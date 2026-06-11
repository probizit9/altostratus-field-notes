# Why does Kueue keep a multi-pod workload Pending even when there is clearly capacity, and how do you debug it?

> **Direct answer.** Kueue keeping a multi-pod workload Pending even when there's clearly capacity is usually a ResourceFlavor that doesn't match the workload's node selector exactly, or a PodGroup `waitFor` value missing some members. The Workload object's status conditions tell the real story — the per-pod status is misleading.

**Topic:** `scheduling` &nbsp;·&nbsp; **Pattern ID:** `kueue-podgroup-stuck-pending` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Kueue keeps a multi-pod workload Pending even when there's clearly capacity

## Root-cause pattern

ResourceFlavor doesn't match the node selector exactly; or PodGroup waitFor missing some pods

## Variants seen in production

- Describe the Workload object, not just the pods
- Status conditions tell the real story
- Worth setting a debug ClusterQueue with broad flavors to isolate

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
      "name": "Why does Kueue keep a multi-pod workload Pending even when there is clearly capacity, and how do you debug it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Kueue keeping a multi-pod workload Pending even when there's clearly capacity is usually a ResourceFlavor that doesn't match the workload's node selector exactly, or a PodGroup `waitFor` value missing some members. The Workload object's status conditions tell the real story \u2014 the per-pod status is misleading."
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
  "headline": "Why does Kueue keep a multi-pod workload Pending even when there is clearly capacity, and how do you debug it?",
  "abstract": "Kueue keeping a multi-pod workload Pending even when there's clearly capacity is usually a ResourceFlavor that doesn't match the workload's node selector exactly, or a PodGroup `waitFor` value missing some members. The Workload object's status conditions tell the real story \u2014 the per-pod status is m",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/scheduling/kueue-podgroup-stuck-pending.md",
  "about": [
    {
      "@type": "Thing",
      "name": "scheduling"
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
  "keywords": "scheduling, kueue, podgroup, stuck, pending, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
