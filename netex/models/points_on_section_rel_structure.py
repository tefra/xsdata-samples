from dataclasses import dataclass, field
from typing import List
from .point_on_line_section import PointOnLineSection
from .point_on_section import PointOnSection
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointsOnSectionRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pointsOnSection_RelStructure"

    point_on_line_section: List[PointOnLineSection] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLineSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_on_section: List[PointOnSection] = field(
        default_factory=list,
        metadata={
            "name": "PointOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
