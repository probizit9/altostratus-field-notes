# Ceph OSDs randomly slow down under sustained training I/O

**Topic:** storage

## Pattern

BlueStore RocksDB compaction blocks foreground writes; you see slow ops in the manager dashboard

## Variants

- bluestore_rocksdb_options tuning: max_background_jobs, write_buffer_size
- DB+WAL on separate NVMe vs collocated with data — different failure modes
- Compaction storms cluster-wide when N OSDs all hit the threshold at once

## Resolution hints

*Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

## Tags

`storage` `ceph-osd-bluestore-rocksdb-stall`

---

*From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
