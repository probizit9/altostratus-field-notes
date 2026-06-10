# Run:AI scheduler silently ignores a new project's quota

**Topic:** runai

## Pattern

Department overprovisioning policy doesn't propagate to projects created after the department

## Variants

- Pods admitted, jobs run, the quota counter never moves
- Webhook that propagates the binding fires at department-create, not project-create
- Any project added later inherits nothing

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`runai` `runai-quota-ignored`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
