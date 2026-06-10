# Cross-node pod traffic silently drops large packets on RKE2 with Cilium

**Topic:** rke2

## Pattern

Underlay MTU and pod-to-pod overlay MTU mismatch; PMTU discovery blocked by IPSec or VXLAN encapsulation

## Variants

- Small payloads work, training all-reduce times out
- ip link show ; ethtool -m show ; trace path with iperf3 -M 1300 confirms it
- Bump cluster MTU to match underlay - overhead, redeploy CNI

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`rke2` `rke2-cni-mtu-drop`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
