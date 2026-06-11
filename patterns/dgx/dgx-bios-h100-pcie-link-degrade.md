# Why does a DGX H100 show PCIe link width x8 instead of x16 after a firmware update, and how do you restore full bandwidth?

> **Direct answer.** A DGX H100 showing PCIe link width x8 instead of x16 after a firmware update is usually a BIOS-level PCIe lane bifurcation defaulted back to auto. Variants: a PCIe retimer firmware mismatch, an NVSwitch link training delay that races with kernel PCIe enumeration, or a bifurcation override that didn't survive the update.

**Topic:** `dgx` &nbsp;·&nbsp; **Pattern ID:** `dgx-bios-h100-pcie-link-degrade` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

After a firmware update on a DGX H100, one GPU shows PCIe link width x8 instead of x16

## Root-cause pattern

BIOS option for PCIe lane bifurcation reset to default; lane assignment changed

## Variants seen in production

- nvidia-smi --query-gpu=pcie.link.width.current still shows the degradation
- Re-applying NVIDIA's reference BIOS config sequence fixes it
- Don't trust 'firmware up to date' — check the actual setting

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
      "name": "Why does a DGX H100 show PCIe link width x8 instead of x16 after a firmware update, and how do you restore full bandwidth?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A DGX H100 showing PCIe link width x8 instead of x16 after a firmware update is usually a BIOS-level PCIe lane bifurcation defaulted back to auto. Variants: a PCIe retimer firmware mismatch, an NVSwitch link training delay that races with kernel PCIe enumeration, or a bifurcation override that didn't survive the update."
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
  "headline": "Why does a DGX H100 show PCIe link width x8 instead of x16 after a firmware update, and how do you restore full bandwidth?",
  "abstract": "A DGX H100 showing PCIe link width x8 instead of x16 after a firmware update is usually a BIOS-level PCIe lane bifurcation defaulted back to auto. Variants: a PCIe retimer firmware mismatch, an NVSwitch link training delay that races with kernel PCIe enumeration, or a bifurcation override that didn'",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/dgx/dgx-bios-h100-pcie-link-degrade.md",
  "about": [
    {
      "@type": "Thing",
      "name": "dgx"
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
  "keywords": "dgx, dgx, bios, h100, pcie, link, degrade, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
