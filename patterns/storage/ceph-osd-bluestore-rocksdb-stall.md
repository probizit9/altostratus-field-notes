# Why do Ceph OSDs randomly stall under sustained training I/O, and how do you stabilize BlueStore + RocksDB?

> **Direct answer.** Ceph OSDs stalling under sustained training I/O are almost always RocksDB compaction backpressure on BlueStore, not raw disk pressure. Variants: WAL on the same device as the data column, key-set growth from many small objects, or default `osd_max_backfills` throttling the recovery loop.

**Topic:** `storage` &nbsp;·&nbsp; **Pattern ID:** `ceph-osd-bluestore-rocksdb-stall` &nbsp;·&nbsp; **License:** MIT &nbsp;·&nbsp; **Source:** Altostratus field notes

---

## Symptom

Ceph OSDs randomly slow down under sustained training I/O

## Root-cause pattern

BlueStore RocksDB compaction blocks foreground writes; you see slow ops in the manager dashboard

## Variants seen in production

- bluestore_rocksdb_options tuning: max_background_jobs, write_buffer_size
- DB+WAL on separate NVMe vs collocated with data — different failure modes
- Compaction storms cluster-wide when N OSDs all hit the threshold at once

## How to confirm

The Workload/Pod/Job status object — not the surface error — is where the real story is. Start there, then move to per-component logs.

## Resolution hints

The variants above are the cleanest fingerprints. Sequential bisection over them (rule out network, then rule out scheduler, then rule out driver) is faster than reading the trainer log line-by-line.

For a full, cited resolution path on this exact issue — including the diagnostic commands and the rollout-safe fix order — open a live session at [altostratus.bot](https://altostratus.bot).

---

## Need this resolved end-to-end?

[**Buy a resolved issue — $99 with refund if unresolved**](https://altostratus.bot/signup?sku=resolved-issue)

Live 30-minute session: voice + camera + text. Every answer cites the corpus; the agent refuses to invent when ungrounded. Refund in one click if we don't resolve it.

---

## Related patterns

- [GPFS token storm on checkpoint](../storage/gpfs-token-storm-on-checkpoint.md)
- [DCGM metrics ≠ nvidia-smi](../observability/victoriametrics-gpu-mismatch.md)
- [Harbor silent tag prune on quota hit](../registry/harbor-quota-silent-tag-prune.md)

Or browse the [full pattern index](../../patterns/README.md).

## Updates

- 📢 New patterns drop on Telegram first — [t.me/altostratus_ai](https://t.me/altostratus_ai)
- 🤖 Ask any pattern in any chat — [@altostratus_consult_bot](https://t.me/altostratus_consult_bot) (inline mode)
- 🌐 The live consultant — [altostratus.bot](https://altostratus.bot)

---

## Author

**AmiHai Habani** — Senior AI-infrastructure architect (DGX, RKE2/OpenShift, Run:AI, Slurm, NCCL). Three years of production engagements across Israeli and US AI teams.

Contact: [amihai.oneman@gmail.com](mailto:amihai.oneman@gmail.com) · [altostratus.bot](https://altostratus.bot)

---

<!-- JSON-LD: FAQPage -->
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do Ceph OSDs randomly stall under sustained training I/O, and how do you stabilize BlueStore + RocksDB?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ceph OSDs stalling under sustained training I/O are almost always RocksDB compaction backpressure on BlueStore, not raw disk pressure. Variants: WAL on the same device as the data column, key-set growth from many small objects, or default `osd_max_backfills` throttling the recovery loop."
      }
    }
  ]
}
```

<!-- JSON-LD: TechArticle -->
```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Why do Ceph OSDs randomly stall under sustained training I/O, and how do you stabilize BlueStore + RocksDB?",
  "abstract": "Ceph OSDs stalling under sustained training I/O are almost always RocksDB compaction backpressure on BlueStore, not raw disk pressure. Variants: WAL on the same device as the data column, key-set growth from many small objects, or default `osd_max_backfills` throttling the recovery loop.",
  "author": {
    "@type": "Person",
    "name": "AmiHai Habani",
    "email": "amihai.oneman@gmail.com",
    "url": "https://altostratus.bot",
    "description": "Senior AI-infrastructure architect (DGX, RKE2/OpenShift, Run:AI, Slurm, NCCL). Three years of production engagements across Israeli and US AI teams."
  },
  "publisher": {
    "@type": "Organization",
    "name": "Altostratus",
    "url": "https://altostratus.bot"
  },
  "url": "https://github.com/probizit9/altostratus-field-notes/blob/main/patterns/storage/ceph-osd-bluestore-rocksdb-stall.md",
  "about": [
    {
      "@type": "Thing",
      "name": "storage"
    },
    {
      "@type": "Thing",
      "name": "AI infrastructure"
    },
    {
      "@type": "Thing",
      "name": "GPU clusters"
    }
  ],
  "keywords": "storage, ceph, osd, bluestore, rocksdb, stall, production AI infrastructure",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true
}
```
