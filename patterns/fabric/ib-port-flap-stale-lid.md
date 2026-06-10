# After an InfiniBand port flap, one rank intermittently can't reach the others

**Topic:** fabric

## Pattern

Subnet manager re-assigned LID; OFED userspace cached the old one

## Variants

- ibstat shows up, ping_pong works to half the cluster
- Restart of OFED tools clears it; ibrebalance-style reload is the fix
- Repeats every time the subnet manager re-elects

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`fabric` `ib-port-flap-stale-lid`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
