# GPU metrics scraped via DCGM-exporter don't match nvidia-smi snapshots

**Topic:** observability

## Pattern

Scrape interval vs DCGM internal counter reset cadence; you're observing a different aggregation window

## Variants

- DCGM has its own gauge reset on field reading
- VictoriaMetrics scrape_interval must align with DCGM's collection window
- Compare with NVML directly to debug

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`observability` `victoriametrics-gpu-mismatch`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
