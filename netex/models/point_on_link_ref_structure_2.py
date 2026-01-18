from __future__ import annotations

from dataclasses import dataclass, field

from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkRefStructure2(PointRefStructure):
    class Meta:
        name = "PointOnLinkRefStructure_"

    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
