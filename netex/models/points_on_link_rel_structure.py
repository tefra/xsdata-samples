from dataclasses import dataclass, field
from typing import List, Optional
from .line_string_type import LineStringType
from .point_on_link import PointOnLink
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointsOnLinkRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pointsOnLink_RelStructure"

    point_on_link: List[PointOnLink] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    line_string: Optional[LineStringType] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
