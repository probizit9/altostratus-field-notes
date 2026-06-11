# After an InfiniBand port flap, why can one rank no longer reach the others and how do you clear the stale LID?

> **Direct answer.** When an InfiniBand port flap leaves one rank unable to reach others, the rank is holding a stale unicast LID in its userspace cache while the SM has issued a new LID after re-discovery. Variants we see: the SM re-LID'd silently after a sweep, the subnet manager failover changed LID ranges, or a multicast group rejoin failed leaving the rank in a half-broken state.

**Topic:** `fabric` &nbsp;·&nbsp; **Pattern ID:** `ib-port-flap-stale-lid` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

After an InfiniBand port flap, one rank intermittently can't reach the others

## Root-cause pattern

Subnet manager re-assigned LID; OFED userspace cached the old one

## Variants seen in production

- ibstat shows up, ping_pong works to half the cluster
- Restart of OFED tools clears it; ibrebalance-style reload is the fix
- Repeats every time the subnet manager re-elects

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
      "name": "After an InfiniBand port flap, why can one rank no longer reach the others and how do you clear the stale LID?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When an InfiniBand port flap leaves one rank unable to reach others, the rank is holding a stale unicast LID in its userspace cache while the SM has issued a new LID after re-discovery. Variants we see: the SM re-LID'd silently after a sweep, the subnet manager failover changed LID ranges, or a multicast group rejoin failed leaving the rank in a half-broken state."
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
  "headline": "After an InfiniBand port flap, why can one rank no longer reach the others and how do you clear the stale LID?",
  "abstract": "When an InfiniBand port flap leaves one rank unable to reach others, the rank is holding a stale unicast LID in its userspace cache while the SM has issued a new LID after re-discovery. Variants we see: the SM re-LID'd silently after a sweep, the subnet manager failover changed LID ranges, or a mult",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/fabric/ib-port-flap-stale-lid.md",
  "about": [
    {
      "@type": "Thing",
      "name": "fabric"
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
  "keywords": "fabric, ib, port, flap, stale, lid, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
