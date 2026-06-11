# Why does the GPU Operator on OpenShift fall back to a CPU image after a kernel patch, and how do you pin the driver?

> **Direct answer.** GPU Operator on OpenShift falling back to a CPU image after a kernel patch is the driver container failing to find a matching pre-compiled module — and the daemonset's toleration excluding the upgraded node. Fix is usually pinning rhcos kernel to a known-good level, or switching to driver-toolkit-aware ClusterPolicy operands.

**Topic:** `openshift` &nbsp;·&nbsp; **Pattern ID:** `openshift-gpu-operator-driver-pin` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

GPU Operator on OpenShift falls back to a CPU image after a kernel patch

## Root-cause pattern

Driver container couldn't find matching pre-compiled module; daemonset toleration excluded the right node

## Variants seen in production

- Check ClusterPolicy operands: nvidia.com/gpu.deploy.driver=true
- rhcos kernel pinned to a level the driver container doesn't have prebuilt — needs gpu-operator-resources annotation
- Worth keeping a hot spare with prior kernel for rapid rollback

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
- [Slurm GRES GPU undercount](../slurm/slurm-gres-gpu-undercount.md)
- [Run:AI quota silently ignored](../runai/runai-quota-ignored.md)

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
      "name": "Why does the GPU Operator on OpenShift fall back to a CPU image after a kernel patch, and how do you pin the driver?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "GPU Operator on OpenShift falling back to a CPU image after a kernel patch is the driver container failing to find a matching pre-compiled module \u2014 and the daemonset's toleration excluding the upgraded node. Fix is usually pinning rhcos kernel to a known-good level, or switching to driver-toolkit-aware ClusterPolicy operands."
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
  "headline": "Why does the GPU Operator on OpenShift fall back to a CPU image after a kernel patch, and how do you pin the driver?",
  "abstract": "GPU Operator on OpenShift falling back to a CPU image after a kernel patch is the driver container failing to find a matching pre-compiled module \u2014 and the daemonset's toleration excluding the upgraded node. Fix is usually pinning rhcos kernel to a known-good level, or switching to driver-toolkit-aw",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/openshift/openshift-gpu-operator-driver-pin.md",
  "about": [
    {
      "@type": "Thing",
      "name": "openshift"
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
  "keywords": "openshift, openshift, gpu, operator, driver, pin, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
