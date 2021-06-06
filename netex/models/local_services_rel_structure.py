from dataclasses import dataclass, field
from typing import List
from .assistance_booking_service import AssistanceBookingService
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service import AssistanceService
from .assistance_service_ref import AssistanceServiceRef
from .catering_service import CateringService
from .catering_service_ref import CateringServiceRef
from .communication_service import CommunicationService
from .communication_service_ref import CommunicationServiceRef
from .complaints_service import ComplaintsService
from .complaints_service_ref import ComplaintsServiceRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_service import CustomerService
from .customer_service_ref import CustomerServiceRef
from .hire_service import HireService
from .hire_service_ref import HireServiceRef
from .left_luggage_service import LeftLuggageService
from .left_luggage_service_ref import LeftLuggageServiceRef
from .local_service import LocalService
from .local_service_ref import LocalServiceRef
from .lost_property_service import LostPropertyService
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_service import LuggageService
from .luggage_service_ref import LuggageServiceRef
from .meeting_point_service import MeetingPointService
from .meeting_point_service_ref import MeetingPointServiceRef
from .money_service import MoneyService
from .money_service_ref import MoneyServiceRef
from .retail_service import RetailService
from .retail_service_ref import RetailServiceRef
from .ticketing_service import TicketingService
from .ticketing_service_ref import TicketingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LocalServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "localServices_RelStructure"

    assistance_booking_service_ref: List[AssistanceBookingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    catering_service_ref: List[CateringServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CateringServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_service_ref: List[RetailServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    money_service_ref: List[MoneyServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "MoneyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hire_service_ref: List[HireServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "HireServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    communication_service_ref: List[CommunicationServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meeting_point_service_ref: List[MeetingPointServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "MeetingPointServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    left_luggage_service_ref: List[LeftLuggageServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LeftLuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_service_ref: List[LuggageServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lost_property_service_ref: List[LostPropertyServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LostPropertyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complaints_service_ref: List[ComplaintsServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "ComplaintsServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_service_ref: List[CustomerServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_service_ref: List[AssistanceServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_service_ref: List[TicketingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_service_ref: List[LocalServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LocalServiceRef",
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
    catering_service: List[CateringService] = field(
        default_factory=list,
        metadata={
            "name": "CateringService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_service: List[RetailService] = field(
        default_factory=list,
        metadata={
            "name": "RetailService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    money_service: List[MoneyService] = field(
        default_factory=list,
        metadata={
            "name": "MoneyService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hire_service: List[HireService] = field(
        default_factory=list,
        metadata={
            "name": "HireService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    communication_service: List[CommunicationService] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meeting_point_service: List[MeetingPointService] = field(
        default_factory=list,
        metadata={
            "name": "MeetingPointService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lost_property_service: List[LostPropertyService] = field(
        default_factory=list,
        metadata={
            "name": "LostPropertyService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    left_luggage_service: List[LeftLuggageService] = field(
        default_factory=list,
        metadata={
            "name": "LeftLuggageService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complaints_service: List[ComplaintsService] = field(
        default_factory=list,
        metadata={
            "name": "ComplaintsService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_service: List[CustomerService] = field(
        default_factory=list,
        metadata={
            "name": "CustomerService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_service: List[LuggageService] = field(
        default_factory=list,
        metadata={
            "name": "LuggageService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_service: List[AssistanceService] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_service: List[TicketingService] = field(
        default_factory=list,
        metadata={
            "name": "TicketingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_service: List[LocalService] = field(
        default_factory=list,
        metadata={
            "name": "LocalService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
