# Argo Events EventSource fires but Sensor never triggers the workflow

**Topic:** platform

## Pattern

Filter expression syntax silently failed; event payload didn't match the dataKey selector

## Variants

- Sensor status shows Triggered: false but no error
- Verbose log on the sensor reveals the JsonPath evaluation
- Always test the dataKey against a real payload sample in argo-events-test

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`platform` `argo-events-stuck-trigger`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
