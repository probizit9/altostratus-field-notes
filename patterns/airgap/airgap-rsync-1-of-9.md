# Air-gapped registry rsync drops one image out of every nine

**Topic:** airgap

## Pattern

Filesystem-side, not rsync-side; inode-allocator stride collision

## Variants

- Same image dropped each cycle; no errors in the rsync log
- Destination NFS inode allocator hits a stride on bastion mount
- Image written, metadata never lands, next pull returns 'manifest not found'
- Switching bastion NFS to nolock,async,nfsvers=4.2 stops the pattern

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`airgap` `airgap-rsync-1-of-9`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
