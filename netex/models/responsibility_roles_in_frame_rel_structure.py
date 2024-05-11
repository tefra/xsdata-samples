from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_role import ResponsibilityRole

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRolesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "responsibilityRolesInFrame_RelStructure"

    responsibility_role: List[ResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
