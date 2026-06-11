# How do you fix NCCL all-reduce hanging at exactly 47% during distributed training?

> **Direct answer.** NCCL all-reduce hanging at exactly the same training-progress percentage every restart is almost always a network-level mismatch one rank can see but the trainer can't surface. The three patterns we see most often: a NIC bond with mismatched MTU between two nodes, a switch port that quietly negotiated 100G while the rest of the fabric stayed at 200G, or an InfiniBand unicast LID that changed after a port flap so one rank holds a stale routing table.

**Topic:** `nccl` &nbsp;·&nbsp; **Pattern ID:** `nccl-allreduce-hang-47` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

NCCL all-reduce hangs at exactly 47% of training

## Root-cause pattern

Network-level mismatch one rank can see but the trainer can't surface

## Variants seen in production

- NIC bond with mismatched MTU between two nodes
- Switch port quietly negotiated to 100G while the rest stayed at 200G
- IB unicast LID changed after a port flap and one rank now has a stale routing table

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
      "name": "How do you fix NCCL all-reduce hanging at exactly 47% during distributed training?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "NCCL all-reduce hanging at exactly the same training-progress percentage every restart is almost always a network-level mismatch one rank can see but the trainer can't surface. The three patterns we see most often: a NIC bond with mismatched MTU between two nodes, a switch port that quietly negotiated 100G while the rest of the fabric stayed at 200G, or an InfiniBand unicast LID that changed after a port flap so one rank holds a stale routing table."
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
  "headline": "How do you fix NCCL all-reduce hanging at exactly 47% during distributed training?",
  "abstract": "NCCL all-reduce hanging at exactly the same training-progress percentage every restart is almost always a network-level mismatch one rank can see but the trainer can't surface. The three patterns we see most often: a NIC bond with mismatched MTU between two nodes, a switch port that quietly negotiat",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/nccl/nccl-allreduce-hang-47.md",
  "about": [
    {
      "@type": "Thing",
      "name": "nccl"
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
  "keywords": "nccl, nccl, allreduce, hang, 47, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
