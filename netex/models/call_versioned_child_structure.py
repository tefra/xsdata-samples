from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .arrival_structure import ArrivalStructure
from .booking_arrangements_structure import BookingArrangementsStructure
from .departure_structure import DepartureStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .flexible_point_properties import FlexiblePointProperties
from .frequency_structure import FrequencyStructure
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .onward_service_link_view import OnwardServiceLinkView
from .onward_timing_link_view import OnwardTimingLinkView
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from .passenger_carrying_requirements_view import PassengerCarryingRequirementsView
from .point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure
from .request_method_type_enumeration import RequestMethodTypeEnumeration
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .scheduled_stop_point_view import ScheduledStopPointView
from .service_journey_ref import ServiceJourneyRef
from .service_link_ref_structure import ServiceLinkRefStructure
from .stop_use_enumeration import StopUseEnumeration
from .template_service_journey_ref import TemplateServiceJourneyRef
from .timing_point_status_enumeration import TimingPointStatusEnumeration
from .train_size import TrainSize
from .vehicle_equipments_rel_structure import VehicleEquipmentsRelStructure
from .vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CallVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "Call_VersionedChildStructure"

    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardTimingLinkView",
                    "type": OnwardTimingLinkView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardServiceLinkRef",
                    "type": ServiceLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardServiceLinkView",
                    "type": OnwardServiceLinkView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointStatus",
                    "type": TimingPointStatusEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Arrival",
                    "type": ArrivalStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Departure",
                    "type": DepartureStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Frequency",
                    "type": FrequencyStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "vias",
                    "type": ViasRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexiblePointProperties",
                    "type": FlexiblePointProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChangeOfDestinationDisplay",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChangeOfServiceRequirements",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestStop",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": False,
                },
                {
                    "name": "RequestMethod",
                    "type": RequestMethodTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": RequestMethodTypeEnumeration.NONE_REQUIRED,
                },
                {
                    "name": "StopUse",
                    "type": StopUseEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingArrangements",
                    "type": BookingArrangementsStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Print",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": True,
                },
                {
                    "name": "Dynamic",
                    "type": DynamicAdvertisementEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": DynamicAdvertisementEnumeration.ALWAYS,
                },
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainSize",
                    "type": TrainSize,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "equipments",
                    "type": VehicleEquipmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Note",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 34,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    constrained: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
