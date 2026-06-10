# Contributing

PRs welcome for new patterns and corrections.

## Pattern template

Create a new file in `patterns/<topic>/<slug>.md` using this exact structure:

```markdown
# <Symptom as a single declarative sentence>

**Topic:** <nccl | runai | airgap | slurm | storage | fabric | inference | openshift | rke2 | registry | dgx | observability | scheduling | platform>

## Pattern

<One paragraph naming the root cause class. Why this happens, not just what.>

## Variants

- <Concrete fingerprint #1 — what to look for to confirm>
- <Variant #2>
- <Variant #3>

## Resolution hints

- <Concrete first thing to try>
- <Backup option>
- <When this isn't the cause — what else to check>

## Tags

`tag1` `tag2` `tag3`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
```

## Voice rules (hard)

These are non-negotiable. PRs that violate them won't merge.

1. **Open with the symptom as a declarative sentence.** No "Have you ever..." preamble.
2. **Refuse to invent.** Only patterns you've actually seen. If you guessed at the cause, drop it.
3. **Concrete fingerprints, not generic advice.** "NIC bond MTU mismatch between two specific nodes" beats "check your network."
4. **Plain text.** No emoji, no exclamation, no engagement-bait phrasing.
5. **≤450 chars total** ideally. Patterns fit inside Telegram channel posts.
6. **No marketing.** No CTAs in the pattern body — those live in the footer.
7. **Cite the root cause class, not the random workaround.** "RocksDB compaction" not "restart the OSD."

## Topics

Use one of: `nccl`, `runai`, `airgap`, `slurm`, `storage`, `fabric`, `inference`, `openshift`, `rke2`, `registry`, `dgx`, `observability`, `scheduling`, `platform`. Open an issue to propose a new topic.

## License

By contributing you agree your contribution is under the [MIT License](LICENSE).
