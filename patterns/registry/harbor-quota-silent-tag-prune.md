# Harbor silently prunes tags when project quota is hit

**Topic:** registry

## Pattern

Garbage-collection policy + retention rule + storage quota interact in a way nobody documented

## Variants

- First the newest pushed image gets deleted, not the oldest
- Distinct from retention rule deletion; logs differ
- Always set hard quota AND retention rule together

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`registry` `harbor-quota-silent-tag-prune`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
