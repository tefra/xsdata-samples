from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.offered_travel_specification import OfferedTravelSpecification
from netex.models.offered_travel_specification_ref import OfferedTravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OfferedTravelSpecificationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "offeredTravelSpecifications_RelStructure"

    offered_travel_specification_ref: List[OfferedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    offered_travel_specification: List[OfferedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
