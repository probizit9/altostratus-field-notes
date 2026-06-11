# Why does Argo Events EventSource fire while the Sensor never triggers the workflow, and how do you trace it?

> **Direct answer.** Argo Events EventSource firing but the Sensor never triggering the workflow is almost always a missing or mismatched dependency name between the EventSource subjects and the Sensor's dependencies block. Variants: EventBus protocol mismatch (NATS vs Jetstream), Sensor trigger conditions evaluated against a stale event object, or RBAC preventing Sensor from creating the workflow.

**Topic:** `platform` &nbsp;·&nbsp; **Pattern ID:** `argo-events-stuck-trigger` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Argo Events EventSource fires but Sensor never triggers the workflow

## Root-cause pattern

Filter expression syntax silently failed; event payload didn't match the dataKey selector

## Variants seen in production

- Sensor status shows Triggered: false but no error
- Verbose log on the sensor reveals the JsonPath evaluation
- Always test the dataKey against a real payload sample in argo-events-test

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
- [Harbor silent tag prune on quota hit](../registry/harbor-quota-silent-tag-prune.md)
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
      "name": "Why does Argo Events EventSource fire while the Sensor never triggers the workflow, and how do you trace it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Argo Events EventSource firing but the Sensor never triggering the workflow is almost always a missing or mismatched dependency name between the EventSource subjects and the Sensor's dependencies block. Variants: EventBus protocol mismatch (NATS vs Jetstream), Sensor trigger conditions evaluated against a stale event object, or RBAC preventing Sensor from creating the workflow."
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
  "headline": "Why does Argo Events EventSource fire while the Sensor never triggers the workflow, and how do you trace it?",
  "abstract": "Argo Events EventSource firing but the Sensor never triggering the workflow is almost always a missing or mismatched dependency name between the EventSource subjects and the Sensor's dependencies block. Variants: EventBus protocol mismatch (NATS vs Jetstream), Sensor trigger conditions evaluated aga",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/platform/argo-events-stuck-trigger.md",
  "about": [
    {
      "@type": "Thing",
      "name": "platform"
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
  "keywords": "platform, argo, events, stuck, trigger, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
