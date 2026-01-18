from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VersionedReference:
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
