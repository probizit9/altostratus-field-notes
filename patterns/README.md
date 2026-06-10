# Patterns

Field notes organized by topic. Each file is one pattern story.

## Index

### NCCL
- [NCCL all-reduce hangs at exactly 47% of training](nccl/nccl-allreduce-hang-47.md)

### Run:AI
- [Run:AI scheduler silently ignores a new project's quota](runai/runai-quota-ignored.md)

### Air-gap
- [Air-gapped registry rsync drops one image out of every nine](airgap/airgap-rsync-1-of-9.md)

### Inference
- [vLLM batch saturates HBM at one tensor-parallel size and not another](inference/vllm-tp-hbm-saturate.md)

### Fabric (IB / RoCE)
- [After an InfiniBand port flap, one rank intermittently can't reach the others](fabric/ib-port-flap-stale-lid.md)

### Slurm
- [Slurm reports fewer GPUs than nvidia-smi sees on a node](slurm/slurm-gres-gpu-undercount.md)

### Storage
- [GPFS shows a token storm every time the trainer hits checkpoint](storage/gpfs-token-storm-on-checkpoint.md)
- [Ceph OSDs randomly slow down under sustained training I/O](storage/ceph-osd-bluestore-rocksdb-stall.md)

### OpenShift
- [GPU Operator on OpenShift falls back to a CPU image after a kernel patch](openshift/openshift-gpu-operator-driver-pin.md)

### RKE2
- [Cross-node pod traffic silently drops large packets on RKE2 with Cilium](rke2/rke2-cni-mtu-drop.md)

### Registry
- [Harbor silently prunes tags when project quota is hit](registry/harbor-quota-silent-tag-prune.md)

### DGX hardware
- [After a firmware update on a DGX H100, one GPU shows PCIe link width x8 instead of x16](dgx/dgx-bios-h100-pcie-link-degrade.md)

### Observability
- [GPU metrics scraped via DCGM-exporter don't match nvidia-smi snapshots](observability/victoriametrics-gpu-mismatch.md)

### Scheduling
- [Kueue keeps a multi-pod workload Pending even when there's clearly capacity](scheduling/kueue-podgroup-stuck-pending.md)

### Platform / GitOps
- [Argo Events EventSource fires but Sensor never triggers the workflow](platform/argo-events-stuck-trigger.md)

---

## Coming next

- More NCCL / RDMA fingerprints
- Slurm cgroups v2 + GPU pinning edge cases
- Lustre OST imbalance fingerprints
- NVLink degradation that nvidia-smi reports as healthy
- NVIDIA Fabric Manager timeout on boot
- MIG mode toggle requiring node reboot
- Flux CD image tag pinning that silently no-ops

→ Subscribe to updates: [t.me/altostratus_ai](https://t.me/altostratus_ai)

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md). The voice rules are non-negotiable.
