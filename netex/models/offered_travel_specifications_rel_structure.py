from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .offered_travel_specification import OfferedTravelSpecification
from .offered_travel_specification_ref import OfferedTravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OfferedTravelSpecificationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "offeredTravelSpecifications_RelStructure"

    offered_travel_specification_ref_or_offered_travel_specification: List[
        Union[OfferedTravelSpecificationRef, OfferedTravelSpecification]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
