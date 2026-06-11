# Why does Run:AI ignore a project's quota and how do you force the scheduler to respect it?

> **Direct answer.** When Run:AI's scheduler silently ignores a project quota, the cause is usually a quota update that was accepted at the API but never propagated to the scheduler decision path — typically a webhook timing race, a department-level quota override that masked the project quota, or a stale cached ProjectAdmission object on the binder.

**Topic:** `runai` &nbsp;·&nbsp; **Pattern ID:** `runai-quota-ignored` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Run:AI scheduler silently ignores a new project's quota

## Root-cause pattern

Department overprovisioning policy doesn't propagate to projects created after the department

## Variants seen in production

- Pods admitted, jobs run, the quota counter never moves
- Webhook that propagates the binding fires at department-create, not project-create
- Any project added later inherits nothing

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

- [Kueue PodGroup stuck Pending](../scheduling/kueue-podgroup-stuck-pending.md)
- [Slurm GRES GPU undercount](../slurm/slurm-gres-gpu-undercount.md)
- [OpenShift GPU Operator driver pin](../openshift/openshift-gpu-operator-driver-pin.md)

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
      "name": "Why does Run:AI ignore a project's quota and how do you force the scheduler to respect it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When Run:AI's scheduler silently ignores a project quota, the cause is usually a quota update that was accepted at the API but never propagated to the scheduler decision path \u2014 typically a webhook timing race, a department-level quota override that masked the project quota, or a stale cached ProjectAdmission object on the binder."
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
  "headline": "Why does Run:AI ignore a project's quota and how do you force the scheduler to respect it?",
  "abstract": "When Run:AI's scheduler silently ignores a project quota, the cause is usually a quota update that was accepted at the API but never propagated to the scheduler decision path \u2014 typically a webhook timing race, a department-level quota override that masked the project quota, or a stale cached Project",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/runai/runai-quota-ignored.md",
  "about": [
    {
      "@type": "Thing",
      "name": "runai"
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
  "keywords": "runai, runai, quota, ignored, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
