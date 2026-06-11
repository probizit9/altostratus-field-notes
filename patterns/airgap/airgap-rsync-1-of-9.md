# Why does an air-gapped container registry rsync drop roughly one image in nine, and how do you fix it?

> **Direct answer.** If an air-gapped container registry rsync drops roughly one image in nine, the cause is almost never the network — it's a deterministic interaction between OCI layer dedup, the rsync block size, and a manifest-index pair that the receiving registry refuses to accept atomically. Common variants are checksum mismatch on a shared layer, a tag race during concurrent push, or a manifest-list (multi-arch) entry that resolves to a layer rsync hasn't yet flushed.

**Topic:** `airgap` &nbsp;·&nbsp; **Pattern ID:** `airgap-rsync-1-of-9` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Air-gapped registry rsync drops one image out of every nine

## Root-cause pattern

Filesystem-side, not rsync-side; inode-allocator stride collision

## Variants seen in production

- Same image dropped each cycle; no errors in the rsync log
- Destination NFS inode allocator hits a stride on bastion mount
- Image written, metadata never lands, next pull returns 'manifest not found'
- Switching bastion NFS to nolock,async,nfsvers=4.2 stops the pattern

## How to confirm

The Workload/Pod/Job status object — not the surface error — is where the real story is. Start there, then move to per-component logs.

## Resolution hints

The variants above are the cleanest fingerprints. Sequential bisection over them (rule out network, then rule out scheduler, then rule out driver) is faster than reading the trainer log line-by-line.

For a full, cited resolution path on this exact issue — including the diagnostic commands and the rollout-safe fix order — open a live session at [altostratus.bot](https://altostratus.bot).

---

## Need this resolved end-to-end?

[**Buy a resolved issue — $99 with refund if unresolved**](https://altostratus.bot/signup?sku=resolved-issue)

Live 30-minute session: voice + camera + text. Every answer cites the corpus; the agent refuses to invent when ungrounded. Refund in one click if we don't resolve it.

---

## Related patterns

Browse the [full pattern index](../../README.md). If a related symptom isn't catalogued yet, [open a PR](../../CONTRIBUTING.md) — contributions welcome.

## Updates

- 📢 New patterns drop on Telegram first — [t.me/altostratus_ai](https://t.me/altostratus_ai)
- 🤖 Ask any pattern in any chat — [@altostratus_consult_bot](https://t.me/altostratus_consult_bot) (inline mode)
- 🌐 The live consultant — [altostratus.bot](https://altostratus.bot)

---

## Author

**AmiHai Habani** — Senior AI-infrastructure architect (DGX, RKE2/OpenShift, Run:AI, Slurm, NCCL). Three years of production engagements across Israeli and US AI teams.

Contact: [amihai.oneman@gmail.com](mailto:amihai.oneman@gmail.com) · [altostratus.bot](https://altostratus.bot)

---

<!-- JSON-LD: FAQPage -->
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does an air-gapped container registry rsync drop roughly one image in nine, and how do you fix it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If an air-gapped container registry rsync drops roughly one image in nine, the cause is almost never the network \u2014 it's a deterministic interaction between OCI layer dedup, the rsync block size, and a manifest-index pair that the receiving registry refuses to accept atomically. Common variants are checksum mismatch on a shared layer, a tag race during concurrent push, or a manifest-list (multi-arch) entry that resolves to a layer rsync hasn't yet flushed."
      }
    }
  ]
}
```

<!-- JSON-LD: TechArticle -->
```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Why does an air-gapped container registry rsync drop roughly one image in nine, and how do you fix it?",
  "abstract": "If an air-gapped container registry rsync drops roughly one image in nine, the cause is almost never the network \u2014 it's a deterministic interaction between OCI layer dedup, the rsync block size, and a manifest-index pair that the receiving registry refuses to accept atomically. Common variants are c",
  "author": {
    "@type": "Person",
    "name": "AmiHai Habani",
    "email": "amihai.oneman@gmail.com",
    "url": "https://altostratus.bot",
    "description": "Senior AI-infrastructure architect (DGX, RKE2/OpenShift, Run:AI, Slurm, NCCL). Three years of production engagements across Israeli and US AI teams."
  },
  "publisher": {
    "@type": "Organization",
    "name": "Altostratus",
    "url": "https://altostratus.bot"
  },
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/airgap/airgap-rsync-1-of-9.md",
  "about": [
    {
      "@type": "Thing",
      "name": "airgap"
    },
    {
      "@type": "Thing",
      "name": "AI infrastructure"
    },
    {
      "@type": "Thing",
      "name": "GPU clusters"
    }
  ],
  "keywords": "airgap, airgap, rsync, 1, of, 9, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
