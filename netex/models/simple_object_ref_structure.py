from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleObjectRefStructure:
    value: str = field(default="")
    ref: str = field(
        metadata={
            "type": "Attribute",
        }
    )
