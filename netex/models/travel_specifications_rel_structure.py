from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .offered_travel_specification import OfferedTravelSpecification
from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .requested_travel_specification import RequestedTravelSpecification
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .travel_specification_1 import TravelSpecification1
from .travel_specification_2 import TravelSpecification2
from .travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "travelSpecifications_RelStructure"

    travel_specification_ref_or_travel_specification: List[
        Union[
            OfferedTravelSpecificationRef,
            RequestedTravelSpecificationRef,
            TravelSpecificationRef,
            OfferedTravelSpecification,
            RequestedTravelSpecification,
            TravelSpecification1,
            TravelSpecification2,
        ]
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
                    "name": "RequestedTravelSpecificationRef",
                    "type": RequestedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationRef",
                    "type": TravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecification",
                    "type": RequestedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification",
                    "type": TravelSpecification1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification_",
                    "type": TravelSpecification2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
