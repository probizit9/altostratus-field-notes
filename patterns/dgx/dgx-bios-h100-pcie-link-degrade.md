# After a firmware update on a DGX H100, one GPU shows PCIe link width x8 instead of x16

**Topic:** dgx

## Pattern

BIOS option for PCIe lane bifurcation reset to default; lane assignment changed

## Variants

- nvidia-smi --query-gpu=pcie.link.width.current still shows the degradation
- Re-applying NVIDIA's reference BIOS config sequence fixes it
- Don't trust 'firmware up to date' — check the actual setting

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`dgx` `dgx-bios-h100-pcie-link-degrade`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
