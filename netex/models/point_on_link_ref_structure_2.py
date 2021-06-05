from dataclasses import dataclass, field
from typing import Optional
from netex.models.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkRefStructure2(PointRefStructure):
    class Meta:
        name = "PointOnLinkRefStructure_"

    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
