from dataclasses import dataclass, field
from typing import List
from .point_on_line_section import PointOnLineSection
from .point_on_section_1 import PointOnSection1
from .point_on_section_2 import PointOnSection2
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
            "min_occurs": 1,
        }
    )
    point_on_section: List[PointOnSection1] = field(
        default_factory=list,
        metadata={
            "name": "PointOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_point_on_section: List[PointOnSection2] = field(
        default_factory=list,
        metadata={
            "name": "PointOnSection_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
