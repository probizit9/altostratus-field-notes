# NCCL all-reduce hangs at exactly 47% of training

**Topic:** nccl

## Pattern

Network-level mismatch one rank can see but the trainer can't surface

## Variants

- NIC bond with mismatched MTU between two nodes
- Switch port quietly negotiated to 100G while the rest stayed at 200G
- IB unicast LID changed after a port flap and one rank now has a stale routing table

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`nccl` `nccl-allreduce-hang-47`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
