from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.offered_travel_specification import OfferedTravelSpecification
from netex.models.offered_travel_specification_ref import OfferedTravelSpecificationRef
from netex.models.requested_travel_specification import RequestedTravelSpecification
from netex.models.requested_travel_specification_ref import RequestedTravelSpecificationRef
from netex.models.travel_specification_1 import TravelSpecification1
from netex.models.travel_specification_2 import TravelSpecification2
from netex.models.travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "travelSpecifications_RelStructure"

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
    offered_travel_specification: List[OfferedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requested_travel_specification: List[RequestedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_travel_specification: List[TravelSpecification2] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
