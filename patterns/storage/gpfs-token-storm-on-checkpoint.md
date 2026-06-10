# GPFS shows a token storm every time the trainer hits checkpoint

**Topic:** storage

## Pattern

Many ranks write small files into the same directory simultaneously; metadata lock contention

## Variants

- Per-rank subdirectory layout reduces it
- Spectrum Scale tuning of maxFilesToCache + maxStatCache helps
- Async checkpointing fundamentally cleaner if the framework supports it

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`storage` `gpfs-token-storm-on-checkpoint`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
