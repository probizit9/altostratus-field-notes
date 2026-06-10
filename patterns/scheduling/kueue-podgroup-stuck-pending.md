# Kueue keeps a multi-pod workload Pending even when there's clearly capacity

**Topic:** scheduling

## Pattern

ResourceFlavor doesn't match the node selector exactly; or PodGroup waitFor missing some pods

## Variants

- Describe the Workload object, not just the pods
- Status conditions tell the real story
- Worth setting a debug ClusterQueue with broad flavors to isolate

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`scheduling` `kueue-podgroup-stuck-pending`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
