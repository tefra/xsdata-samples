from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class CachePartitionType:
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9_]{1,}",
        }
    )
