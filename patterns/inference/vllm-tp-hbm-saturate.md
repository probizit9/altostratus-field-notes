# Why does vLLM OOM on HBM at TP=3 but fit at TP=2 and TP=4, and how do you size around it?

> **Direct answer.** vLLM fitting at TP=2 and TP=4 but OOMing at TP=3 is a KV-cache footprint discontinuity at tensor-parallel boundaries, not a memory leak. Activation layouts fragment across ranks differently per TP value, and a non-power-of-2 TP often produces uneven per-rank slices. The fix is usually to recompute `--max-num-batched-tokens` against the actual per-rank KV slice, not against total HBM.

**Topic:** `inference` &nbsp;·&nbsp; **Pattern ID:** `vllm-tp-hbm-saturate` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

vLLM batch saturates HBM at one tensor-parallel size and not another

## Root-cause pattern

KV-cache footprint discontinuity at TP boundaries

## Variants seen in production

- TP=2 fits, TP=4 fits, TP=3 inexplicably OOMs
- Activation layout fragments across ranks differently per TP
- Worth checking --max-num-batched-tokens against the per-rank KV slice

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

- [DGX H100 PCIe x8 after firmware](../dgx/dgx-bios-h100-pcie-link-degrade.md)
- [DCGM metrics ≠ nvidia-smi](../observability/victoriametrics-gpu-mismatch.md)
- [NCCL all-reduce hang at 47%](../nccl/nccl-allreduce-hang-47.md)

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
      "name": "Why does vLLM OOM on HBM at TP=3 but fit at TP=2 and TP=4, and how do you size around it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "vLLM fitting at TP=2 and TP=4 but OOMing at TP=3 is a KV-cache footprint discontinuity at tensor-parallel boundaries, not a memory leak. Activation layouts fragment across ranks differently per TP value, and a non-power-of-2 TP often produces uneven per-rank slices. The fix is usually to recompute `--max-num-batched-tokens` against the actual per-rank KV slice, not against total HBM."
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
  "headline": "Why does vLLM OOM on HBM at TP=3 but fit at TP=2 and TP=4, and how do you size around it?",
  "abstract": "vLLM fitting at TP=2 and TP=4 but OOMing at TP=3 is a KV-cache footprint discontinuity at tensor-parallel boundaries, not a memory leak. Activation layouts fragment across ranks differently per TP value, and a non-power-of-2 TP often produces uneven per-rank slices. The fix is usually to recompute `",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/inference/vllm-tp-hbm-saturate.md",
  "about": [
    {
      "@type": "Thing",
      "name": "inference"
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
  "keywords": "inference, vllm, tp, hbm, saturate, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
