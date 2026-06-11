# Why does Harbor silently prune image tags when a project quota is hit, and how do you prevent training artifact loss?

> **Direct answer.** Harbor silently pruning tags when a project quota is hit happens because the GC policy considers untagged manifests as deletable, but training artifacts that share layers across runs become untagged when an older run's tag is removed. The fix is to use immutable tag rules and disable retain-no-tag GC, or move artifacts to a dedicated project.

**Topic:** `registry` &nbsp;·&nbsp; **Pattern ID:** `harbor-quota-silent-tag-prune` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Harbor silently prunes tags when project quota is hit

## Root-cause pattern

Garbage-collection policy + retention rule + storage quota interact in a way nobody documented

## Variants seen in production

- First the newest pushed image gets deleted, not the oldest
- Distinct from retention rule deletion; logs differ
- Always set hard quota AND retention rule together

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

- [Air-gapped rsync drops 1 image in 9](../airgap/airgap-rsync-1-of-9.md)
- [Argo Events Sensor never triggers](../platform/argo-events-stuck-trigger.md)
- [Ceph OSD stalls under training I/O](../storage/ceph-osd-bluestore-rocksdb-stall.md)

Or browse the [full pattern index](../../patterns/README.md).

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
      "name": "Why does Harbor silently prune image tags when a project quota is hit, and how do you prevent training artifact loss?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Harbor silently pruning tags when a project quota is hit happens because the GC policy considers untagged manifests as deletable, but training artifacts that share layers across runs become untagged when an older run's tag is removed. The fix is to use immutable tag rules and disable retain-no-tag GC, or move artifacts to a dedicated project."
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
  "headline": "Why does Harbor silently prune image tags when a project quota is hit, and how do you prevent training artifact loss?",
  "abstract": "Harbor silently pruning tags when a project quota is hit happens because the GC policy considers untagged manifests as deletable, but training artifacts that share layers across runs become untagged when an older run's tag is removed. The fix is to use immutable tag rules and disable retain-no-tag G",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/registry/harbor-quota-silent-tag-prune.md",
  "about": [
    {
      "@type": "Thing",
      "name": "registry"
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
  "keywords": "registry, harbor, quota, silent, tag, prune, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
