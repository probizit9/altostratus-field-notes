# Altostratus Field Notes

> Patterns from production AI infrastructure work.
> NVIDIA DGX • RKE2 / OpenShift • Run:AI • Slurm • NCCL.

A public, MIT-licensed sample of the kind of patterns we see in real engagements — between BIOS settings on a DGX H100 and the running training job. NCCL all-reduce hanging at 47%. Run:AI scheduler quietly ignoring a quota. Air-gapped registry rsync dropping one image out of every nine.

We publish patterns here because the patterns themselves should be in the open. **The full corpus (30,358 architect notes) + cited live consulting lives at [altostratus.bot](https://altostratus.bot).**

---

**📢 New patterns drop on Telegram first — [t.me/altostratus_ai](https://t.me/altostratus_ai)**
**🤖 Ask one in any chat — [@altostratus_consult_bot](https://t.me/altostratus_consult_bot) (inline mode)**

---

## What's in here

| Section | What |
|---|---|
| [`patterns/`](patterns/) | Individual pattern stories. One file per pattern. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add your own. We accept community contributions. |
| [`scripts/`](scripts/) | Helpers for converting source corpus → published markdown. |

Each pattern follows a strict template:

- **Symptom** — the visible failure
- **Pattern** — the root cause class
- **Variants** — concrete fingerprints to look for
- **Resolution hints** — what to try first
- **Tags** — for cross-referencing

We refuse to invent. If a pattern record doesn't cite something we've actually seen, we don't publish it.

---

## About

[Altostratus](https://altostratus.bot) is an AI consultant trained on three years of senior AI-infrastructure architect notes. Voice + camera + text — live 30-minute sessions with cited answers.

Per-resolved-issue pricing ($99) with refund guarantee. Team plan at $299/month.

This repo is a public sample of the same kind of pattern thinking, given away because the patterns aren't the moat — applied judgment in a live session is.

---

## Updates

| Channel | What |
|---|---|
| 📢 **[t.me/altostratus_ai](https://t.me/altostratus_ai)** | Telegram channel — new pattern every Tue + Thu |
| 🌐 **[altostratus.bot](https://altostratus.bot)** | The live consultant + the corpus product |

---

## Topics covered

- **NVIDIA DGX** — racking, IB cabling, BIOS, firmware, NVLink, MIG, NVML
- **Kubernetes / RKE2 / OpenShift** — bare metal, CNI, ingress, admission
- **Run:AI** — scheduler, quotas, fractional GPU, project policies
- **Slurm** — gres, prologue/epilogue, cgroups v2, accounting
- **NCCL / IB / RoCE** — all-reduce, port flaps, LID changes, MTU
- **Storage** — Lustre, GPFS, VAST, Ceph, BlueStore, RocksDB
- **MLOps platforms** — Kueue, Argo, vLLM, Flux, Helm, GPU Operator
- **Air-gap** — registry mirroring, bastion patterns, rsync edge cases
- **Observability** — DCGM, Prometheus, VictoriaMetrics, GPU telemetry

---

## License

MIT — see [LICENSE](LICENSE). Patterns are field notes, freely usable.

---

## Behind it

AmiHai Habani — senior AI-infrastructure architect, Israel. Three years of self-driven engagements across DGX clusters, scheduler tuning, air-gapped deployments, GPU observability.

The patterns here are a sample of how we think. The product is the live session.

→ [altostratus.bot](https://altostratus.bot)
