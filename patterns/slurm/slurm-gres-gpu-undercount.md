# Slurm reports fewer GPUs than nvidia-smi sees on a node

**Topic:** slurm

## Pattern

gres.conf has stale device file list after a driver upgrade

## Variants

- /dev/nvidia* numbering shifted; gres.conf hardcodes path
- AutoDetect=nvml fixes it, but production might pin manually for reproducibility
- Check slurmd log for 'gres/gpu count of N from configuration' vs nvidia-smi -L

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`slurm` `slurm-gres-gpu-undercount`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
