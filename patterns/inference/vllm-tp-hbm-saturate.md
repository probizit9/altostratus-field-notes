# vLLM batch saturates HBM at one tensor-parallel size and not another

**Topic:** inference

## Pattern

KV-cache footprint discontinuity at TP boundaries

## Variants

- TP=2 fits, TP=4 fits, TP=3 inexplicably OOMs
- Activation layout fragments across ranks differently per TP
- Worth checking --max-num-batched-tokens against the per-rank KV slice

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`inference` `vllm-tp-hbm-saturate`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
