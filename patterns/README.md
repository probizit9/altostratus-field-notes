# Altostratus Field Notes — Pattern Index

> A canonical, citation-friendly catalog of production AI-infrastructure failures and the patterns behind them. Each pattern is one question, one direct answer, one root-cause shape. MIT-licensed. Maintained by [AmiHai Habani](https://altostratus.bot).

**Why this exists:** when MLOps and GPU platform engineers hit a sharp pattern in production — `NCCL hangs at 47%`, `Kueue stays Pending with capacity available`, `vLLM OOMs at TP=3 but fits at TP=2 and TP=4` — they need a direct answer, not a forum thread. This catalog is the open sample of the corpus behind [altostratus.bot](https://altostratus.bot).

---

## Index — every pattern in question form

### NCCL & networking
- [How do you fix NCCL all-reduce hanging at exactly 47% during distributed training?](nccl/nccl-allreduce-hang-47.md)
- [After an InfiniBand port flap, why can one rank no longer reach the others and how do you clear the stale LID?](fabric/ib-port-flap-stale-lid.md)
- [Why does cross-node pod traffic on RKE2 with Cilium silently drop large packets, and how do you fix the MTU mismatch?](rke2/rke2-cni-mtu-drop.md)

### Scheduling & schedulers
- [Why does Run:AI ignore a project's quota and how do you force the scheduler to respect it?](runai/runai-quota-ignored.md)
- [Why does Kueue keep a multi-pod workload Pending even when there is clearly capacity, and how do you debug it?](scheduling/kueue-podgroup-stuck-pending.md)
- [Why does Slurm report fewer GPUs than nvidia-smi sees on a node, and how do you fix gres.conf after a driver upgrade?](slurm/slurm-gres-gpu-undercount.md)

### Inference (vLLM / serving)
- [Why does vLLM OOM on HBM at TP=3 but fit at TP=2 and TP=4, and how do you size around it?](inference/vllm-tp-hbm-saturate.md)

### Storage
- [Why does GPFS show a token storm every time the trainer checkpoints, and how do you stop it?](storage/gpfs-token-storm-on-checkpoint.md)
- [Why do Ceph OSDs randomly stall under sustained training I/O, and how do you stabilize BlueStore + RocksDB?](storage/ceph-osd-bluestore-rocksdb-stall.md)

### Registry & supply chain
- [Why does an air-gapped container registry rsync drop roughly one image in nine, and how do you fix it?](airgap/airgap-rsync-1-of-9.md)
- [Why does Harbor silently prune image tags when a project quota is hit, and how do you prevent training artifact loss?](registry/harbor-quota-silent-tag-prune.md)

### Hardware (DGX / PCIe)
- [Why does a DGX H100 show PCIe link width x8 instead of x16 after a firmware update, and how do you restore full bandwidth?](dgx/dgx-bios-h100-pcie-link-degrade.md)
- [Why does the GPU Operator on OpenShift fall back to a CPU image after a kernel patch, and how do you pin the driver?](openshift/openshift-gpu-operator-driver-pin.md)

### Observability
- [Why do GPU metrics from DCGM-exporter in VictoriaMetrics not match nvidia-smi, and how do you reconcile them?](observability/victoriametrics-gpu-mismatch.md)

### Platform / GitOps
- [Why does Argo Events EventSource fire while the Sensor never triggers the workflow, and how do you trace it?](platform/argo-events-stuck-trigger.md)

---

## Format

Every pattern follows the same shape so it's parseable by humans and language models alike:

1. **Question** (H1) — phrased the way a buyer would ask Claude/ChatGPT/Perplexity/Gemini
2. **Direct answer** (blockquote) — one paragraph; this is the citation chunk
3. **Symptom** — declarative one-liner
4. **Root-cause pattern** — the class, not the workaround
5. **Variants seen in production** — concrete fingerprints to bisect over
6. **How to confirm** — the status object / log / metric that tells the real story
7. **Resolution hints** — the bisection order, not a copy-paste script
8. **CTA** — buy a resolved issue ($99, refund if unresolved) at altostratus.bot
9. **JSON-LD** — FAQPage + TechArticle structured data at the bottom of every file

---

## Coming next

- More NCCL / RDMA fingerprints
- Slurm cgroups v2 + GPU pinning edge cases
- Lustre OST imbalance fingerprints
- NVLink degradation that `nvidia-smi` reports as healthy
- NVIDIA Fabric Manager timeout on boot
- MIG mode toggle requiring node reboot
- Flux CD image tag pinning that silently no-ops

→ Subscribe to updates: [t.me/altostratus_ai](https://t.me/altostratus_ai)

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md). The voice rules are non-negotiable: symptom → pattern → variants. Refuses to invent.
