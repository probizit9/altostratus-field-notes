# Why does Slurm report fewer GPUs than nvidia-smi sees on a node, and how do you fix gres.conf after a driver upgrade?

> **Direct answer.** Slurm reporting fewer GPUs than nvidia-smi sees is usually a stale device-file list in `gres.conf` after a driver upgrade. The `/dev/nvidia*` numbering shifts; `gres.conf` hardcodes the old paths. Setting `AutoDetect=nvml` fixes it cleanly, though production configurations often pin manually for reproducibility.

**Topic:** `slurm` &nbsp;·&nbsp; **Pattern ID:** `slurm-gres-gpu-undercount` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Slurm reports fewer GPUs than nvidia-smi sees on a node

## Root-cause pattern

gres.conf has stale device file list after a driver upgrade

## Variants seen in production

- /dev/nvidia* numbering shifted; gres.conf hardcodes path
- AutoDetect=nvml fixes it, but production might pin manually for reproducibility
- Check slurmd log for 'gres/gpu count of N from configuration' vs nvidia-smi -L

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
      "name": "Why does Slurm report fewer GPUs than nvidia-smi sees on a node, and how do you fix gres.conf after a driver upgrade?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slurm reporting fewer GPUs than nvidia-smi sees is usually a stale device-file list in `gres.conf` after a driver upgrade. The `/dev/nvidia*` numbering shifts; `gres.conf` hardcodes the old paths. Setting `AutoDetect=nvml` fixes it cleanly, though production configurations often pin manually for reproducibility."
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
  "headline": "Why does Slurm report fewer GPUs than nvidia-smi sees on a node, and how do you fix gres.conf after a driver upgrade?",
  "abstract": "Slurm reporting fewer GPUs than nvidia-smi sees is usually a stale device-file list in `gres.conf` after a driver upgrade. The `/dev/nvidia*` numbering shifts; `gres.conf` hardcodes the old paths. Setting `AutoDetect=nvml` fixes it cleanly, though production configurations often pin manually for rep",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/slurm/slurm-gres-gpu-undercount.md",
  "about": [
    {
      "@type": "Thing",
      "name": "slurm"
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
  "keywords": "slurm, slurm, gres, gpu, undercount, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
