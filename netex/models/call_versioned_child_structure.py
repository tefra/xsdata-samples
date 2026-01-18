from dataclasses import dataclass, field
from typing import Optional, Union

from .arrival_structure import ArrivalStructure
from .booking_arrangements_structure import BookingArrangementsStructure
from .departure_structure import DepartureStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .flexible_point_properties import FlexiblePointProperties
from .frequency_structure import FrequencyStructure
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .onward_service_link_view import OnwardServiceLinkView
from .onward_timing_link_view import OnwardTimingLinkView
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from .passenger_carrying_requirements_view import (
    PassengerCarryingRequirementsView,
)
from .point_in_journey_pattern_ref_structure import (
    PointInJourneyPatternRefStructure,
)
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

    visit_number: int | None = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view: FareScheduledStopPointRef | ScheduledStopPointRef | ScheduledStopPointView | None = field(
        default=None,
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
            ),
        },
    )
    onward_timing_link_view: OnwardTimingLinkView | None = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_service_link_ref_or_onward_service_link_view: ServiceLinkRefStructure | OnwardServiceLinkView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    timing_point_status: TimingPointStatusEnumeration | None = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_journey_ref: TemplateServiceJourneyRef | ServiceJourneyRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    point_in_journey_pattern_ref: PointInJourneyPatternRefStructure | None = field(
        default=None,
        metadata={
            "name": "PointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    arrival: ArrivalStructure | None = field(
        default=None,
        metadata={
            "name": "Arrival",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure: DepartureStructure | None = field(
        default=None,
        metadata={
            "name": "Departure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency: FrequencyStructure | None = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_ref_or_destination_display_view: DestinationDisplayRef | DestinationDisplayView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    vias: ViasRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_point_properties: FlexiblePointProperties | None = field(
        default=None,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_destination_display: bool | None = field(
        default=None,
        metadata={
            "name": "ChangeOfDestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_service_requirements: bool | None = field(
        default=None,
        metadata={
            "name": "ChangeOfServiceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: NoticeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_stop: bool | None = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_method: RequestMethodTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "RequestMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_use: StopUseEnumeration | None = field(
        default=None,
        metadata={
            "name": "StopUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_arrangements: BookingArrangementsStructure | None = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    print: bool | None = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dynamic: DynamicAdvertisementEnumeration | None = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view: PassengerCarryingRequirementRef | PassengerCarryingRequirementsView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    train_size: TrainSize | None = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipments: VehicleEquipmentsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    note: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    constrained: bool | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
