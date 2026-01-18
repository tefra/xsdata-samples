from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnLinkByValueStructure:
    distance_from_start: None | Decimal = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
