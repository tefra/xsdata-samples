from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.cache_partition_type import CachePartitionType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class CachePartitionGroupType:
    partition: list[CachePartitionType] = field(
        default_factory=list,
        metadata={
            "name": "Partition",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 2,
        },
    )
