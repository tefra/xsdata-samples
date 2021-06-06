from dataclasses import dataclass, field
from typing import List
from .assistance_booking_service import AssistanceBookingService
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceBookingServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "assistanceBookingServices_RelStructure"

    assistance_booking_service_ref: List[AssistanceBookingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_booking_service: List[AssistanceBookingService] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
