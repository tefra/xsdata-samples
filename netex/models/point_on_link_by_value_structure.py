from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkByValueStructure:
    distance_from_start: Decimal | None = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
