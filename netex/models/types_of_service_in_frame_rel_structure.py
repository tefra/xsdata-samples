from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_service import TypeOfService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfServiceInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfServiceInFrame_RelStructure"

    type_of_service: List[TypeOfService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
