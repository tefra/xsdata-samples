from dataclasses import dataclass, field
from typing import List
from netex.models.access_space import AccessSpace
from netex.models.access_space_ref import AccessSpaceRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessSpaces_RelStructure"

    access_space_ref: List[AccessSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space: List[AccessSpace] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
