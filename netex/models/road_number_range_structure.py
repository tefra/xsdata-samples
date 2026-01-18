from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadNumberRangeStructure:
    from_number: None | int = field(
        default=None,
        metadata={
            "name": "FromNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_number: None | int = field(
        default=None,
        metadata={
            "name": "ToNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
