# GPU Operator on OpenShift falls back to a CPU image after a kernel patch

**Topic:** openshift

## Pattern

Driver container couldn't find matching pre-compiled module; daemonset toleration excluded the right node

## Variants

- Check ClusterPolicy operands: nvidia.com/gpu.deploy.driver=true
- rhcos kernel pinned to a level the driver container doesn't have prebuilt — needs gpu-operator-resources annotation
- Worth keeping a hot spare with prior kernel for rapid rollback

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`openshift` `openshift-gpu-operator-driver-pin`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
