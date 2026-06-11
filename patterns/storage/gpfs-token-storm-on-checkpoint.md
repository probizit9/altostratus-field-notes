# Why does GPFS show a token storm every time the trainer checkpoints, and how do you stop it?

> **Direct answer.** GPFS token storms during trainer checkpoints almost always come from writer contention on the same metadata-region — checkpoints touch many small files in tight time windows, and token revocation cascades across all nodes holding read tokens. Variants: stripe group mis-sized for small-file workload, mmfs metadata-replica contention, or a single checkpoint directory shared across all ranks.

**Topic:** `storage` &nbsp;·&nbsp; **Pattern ID:** `gpfs-token-storm-on-checkpoint` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

GPFS shows a token storm every time the trainer hits checkpoint

## Root-cause pattern

Many ranks write small files into the same directory simultaneously; metadata lock contention

## Variants seen in production

- Per-rank subdirectory layout reduces it
- Spectrum Scale tuning of maxFilesToCache + maxStatCache helps
- Async checkpointing fundamentally cleaner if the framework supports it

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
      "name": "Why does GPFS show a token storm every time the trainer checkpoints, and how do you stop it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "GPFS token storms during trainer checkpoints almost always come from writer contention on the same metadata-region \u2014 checkpoints touch many small files in tight time windows, and token revocation cascades across all nodes holding read tokens. Variants: stripe group mis-sized for small-file workload, mmfs metadata-replica contention, or a single checkpoint directory shared across all ranks."
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
  "headline": "Why does GPFS show a token storm every time the trainer checkpoints, and how do you stop it?",
  "abstract": "GPFS token storms during trainer checkpoints almost always come from writer contention on the same metadata-region \u2014 checkpoints touch many small files in tight time windows, and token revocation cascades across all nodes holding read tokens. Variants: stripe group mis-sized for small-file workload,",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/storage/gpfs-token-storm-on-checkpoint.md",
  "about": [
    {
      "@type": "Thing",
      "name": "storage"
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
  "keywords": "storage, gpfs, token, storm, on, checkpoint, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
