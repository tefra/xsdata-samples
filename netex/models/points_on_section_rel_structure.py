from dataclasses import dataclass, field
from typing import List, Union

from .point_on_line_section import PointOnLineSection
from .point_on_section_1 import PointOnSection1
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointsOnSectionRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pointsOnSection_RelStructure"

    point_on_section: List[Union[PointOnLineSection, PointOnSection1]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOnLineSection",
                    "type": PointOnLineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnSection",
                    "type": PointOnSection1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
