from dataclasses import dataclass, field
from typing import List
from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "travelSpecificationRefs_RelStructure"

    offered_travel_specification_ref: List[OfferedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requested_travel_specification_ref: List[RequestedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification_ref: List[TravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
