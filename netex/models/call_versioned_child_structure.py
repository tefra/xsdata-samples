from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.booking_arrangements_structure import BookingArrangementsStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_display_view import DestinationDisplayView
from netex.models.dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.flexible_point_properties import FlexiblePointProperties
from netex.models.frequency_structure import FrequencyStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.onward_service_link_view import OnwardServiceLinkView
from netex.models.onward_timing_link_view import OnwardTimingLinkView
from netex.models.passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from netex.models.passenger_carrying_requirements_view import PassengerCarryingRequirementsView
from netex.models.point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure
from netex.models.request_method_type_enumeration import RequestMethodTypeEnumeration
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_view import ScheduledStopPointView
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.stop_use_enumeration import StopUseEnumeration
from netex.models.template_service_journey_ref import TemplateServiceJourneyRef
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.train_size import TrainSize
from netex.models.vehicle_equipments_rel_structure import VehicleEquipmentsRelStructure
from netex.models.vias_rel_structure import ViasRelStructure

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
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_timing_link_view: Optional[OnwardTimingLinkView] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_service_link_ref: Optional[ServiceLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_service_link_view: Optional[OnwardServiceLinkView] = field(
        default=None,
        metadata={
            "name": "OnwardServiceLinkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_status: Optional[TimingPointStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    service_journey_ref: Optional[ServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_in_journey_pattern_ref: Optional[PointInJourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "PointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival: Optional[ArrivalStructure] = field(
        default=None,
        metadata={
            "name": "Arrival",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure: Optional[DepartureStructure] = field(
        default=None,
        metadata={
            "name": "Departure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_point_properties: Optional[FlexiblePointProperties] = field(
        default=None,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_destination_display: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfDestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_service_requirements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfServiceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_method: Optional[RequestMethodTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RequestMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_use: Optional[StopUseEnumeration] = field(
        default=None,
        metadata={
            "name": "StopUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_carrying_requirement_ref: Optional[PassengerCarryingRequirementRef] = field(
        default=None,
        metadata={
            "name": "PassengerCarryingRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_carrying_requirements_view: Optional[PassengerCarryingRequirementsView] = field(
        default=None,
        metadata={
            "name": "PassengerCarryingRequirementsView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipments: Optional[VehicleEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
