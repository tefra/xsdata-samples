from dataclasses import dataclass, field
from typing import List, Union

from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "travelSpecificationRefs_RelStructure"

    travel_specification_ref: List[
        Union[
            OfferedTravelSpecificationRef,
            RequestedTravelSpecificationRef,
            TravelSpecificationRef,
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
            ),
        },
    )
