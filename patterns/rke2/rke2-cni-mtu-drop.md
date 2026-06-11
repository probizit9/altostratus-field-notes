# Why does cross-node pod traffic on RKE2 with Cilium silently drop large packets, and how do you fix the MTU mismatch?

> **Direct answer.** Cross-node pod traffic on RKE2 with Cilium silently dropping large packets is an underlay-vs-overlay MTU mismatch. Small payloads work, training all-reduce times out, and `iperf3 -M 1300` confirms it. The fix is to bump the CNI MTU to match the underlay minus the encap overhead, then redeploy.

**Topic:** `rke2` &nbsp;·&nbsp; **Pattern ID:** `rke2-cni-mtu-drop` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Cross-node pod traffic silently drops large packets on RKE2 with Cilium

## Root-cause pattern

Underlay MTU and pod-to-pod overlay MTU mismatch; PMTU discovery blocked by IPSec or VXLAN encapsulation

## Variants seen in production

- Small payloads work, training all-reduce times out
- ip link show ; ethtool -m show ; trace path with iperf3 -M 1300 confirms it
- Bump cluster MTU to match underlay - overhead, redeploy CNI

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
      "name": "Why does cross-node pod traffic on RKE2 with Cilium silently drop large packets, and how do you fix the MTU mismatch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cross-node pod traffic on RKE2 with Cilium silently dropping large packets is an underlay-vs-overlay MTU mismatch. Small payloads work, training all-reduce times out, and `iperf3 -M 1300` confirms it. The fix is to bump the CNI MTU to match the underlay minus the encap overhead, then redeploy."
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
  "headline": "Why does cross-node pod traffic on RKE2 with Cilium silently drop large packets, and how do you fix the MTU mismatch?",
  "abstract": "Cross-node pod traffic on RKE2 with Cilium silently dropping large packets is an underlay-vs-overlay MTU mismatch. Small payloads work, training all-reduce times out, and `iperf3 -M 1300` confirms it. The fix is to bump the CNI MTU to match the underlay minus the encap overhead, then redeploy.",
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
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/rke2/rke2-cni-mtu-drop.md",
  "about": [
    {
      "@type": "Thing",
      "name": "rke2"
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
  "keywords": "rke2, rke2, cni, mtu, drop, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
