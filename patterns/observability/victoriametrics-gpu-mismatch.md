# Why do GPU metrics from DCGM-exporter in VictoriaMetrics not match nvidia-smi, and how do you reconcile them?

> **Direct answer.** DCGM-exporter metrics not matching nvidia-smi in VictoriaMetrics is almost always a sampling/aggregation interval mismatch combined with the way DCGM scrapes MIG slice metrics differently from whole-GPU metrics. Common variants: scrape interval longer than the metric update window, MIG mode toggled at runtime, or label rewriting that drops the partition_index.

**Topic:** `observability` &nbsp;·&nbsp; **Pattern ID:** `victoriametrics-gpu-mismatch` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

GPU metrics scraped via DCGM-exporter don't match nvidia-smi snapshots

## Root-cause pattern

Scrape interval vs DCGM internal counter reset cadence; you're observing a different aggregation window

## Variants seen in production

- DCGM has its own gauge reset on field reading
- VictoriaMetrics scrape_interval must align with DCGM's collection window
- Compare with NVML directly to debug

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
- [vLLM OOM at TP=3, fits at TP=2/4](../inference/vllm-tp-hbm-saturate.md)
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
      "name": "Why do GPU metrics from DCGM-exporter in VictoriaMetrics not match nvidia-smi, and how do you reconcile them?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "DCGM-exporter metrics not matching nvidia-smi in VictoriaMetrics is almost always a sampling/aggregation interval mismatch combined with the way DCGM scrapes MIG slice metrics differently from whole-GPU metrics. Common variants: scrape interval longer than the metric update window, MIG mode toggled at runtime, or label rewriting that drops the partition_index."
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
  "headline": "Why do GPU metrics from DCGM-exporter in VictoriaMetrics not match nvidia-smi, and how do you reconcile them?",
  "abstract": "DCGM-exporter metrics not matching nvidia-smi in VictoriaMetrics is almost always a sampling/aggregation interval mismatch combined with the way DCGM scrapes MIG slice metrics differently from whole-GPU metrics. Common variants: scrape interval longer than the metric update window, MIG mode toggled ",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/observability/victoriametrics-gpu-mismatch.md",
  "about": [
    {
      "@type": "Thing",
      "name": "observability"
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
  "keywords": "observability, victoriametrics, gpu, mismatch, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
