from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .accessibility_assessment import AccessibilityAssessment
from .common_version_frame_structure import CommonVersionFrameStructure
from .compound_train_ref import CompoundTrainRef
from .contained_availability_conditions_rel_structure import (
    ContainedAvailabilityConditionsRelStructure,
)
from .coupled_journeys_in_frame_rel_structure import (
    CoupledJourneysInFrameRelStructure,
)
from .default_interchanges_in_frame_rel_structure import (
    DefaultInterchangesInFrameRelStructure,
)
from .flexible_service_properties_in_frame_rel_structure import (
    FlexibleServicePropertiesInFrameRelStructure,
)
from .frequency_groups_in_frame_rel_structure import (
    FrequencyGroupsInFrameRelStructure,
)
from .group_of_links_in_frame_rel_structure import (
    GroupOfLinksInFrameRelStructure,
)
from .groups_of_services_in_frame_rel_structure import (
    GroupsOfServicesInFrameRelStructure,
)
from .interchange_rules_in_frame_rel_structure import (
    InterchangeRulesInFrameRelStructure,
)
from .journey_accounting_ref import JourneyAccountingRef
from .journey_accountings_in_frame_rel_structure import (
    JourneyAccountingsInFrameRelStructure,
)
from .journey_interchanges_in_frame_rel_structure import (
    JourneyInterchangesInFrameRelStructure,
)
from .journey_meetings_in_frame_rel_structure import (
    JourneyMeetingsInFrameRelStructure,
)
from .journey_part_couples_in_frame_rel_structure import (
    JourneyPartCouplesInFrameRelStructure,
)
from .journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from .line_view import LineView
from .network_view import NetworkView
from .notice_assignments_in_frame_rel_structure import (
    NoticeAssignmentsInFrameRelStructure,
)
from .notices_in_frame_rel_structure import NoticesInFrameRelStructure
from .operator_view import OperatorView
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_facility_sets_in_frame_rel_structure import (
    ServiceFacilitySetsInFrameRelStructure,
)
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .time_demand_type_assignments_in_frame_rel_structure import (
    TimeDemandTypeAssignmentsInFrameRelStructure,
)
from .time_demand_types_in_frame_rel_structure import (
    TimeDemandTypesInFrameRelStructure,
)
from .train_numbers_in_frame_rel_structure import (
    TrainNumbersInFrameRelStructure,
)
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .types_of_service_in_frame_rel_structure import (
    TypesOfServiceInFrameRelStructure,
)
from .vehicle_journey_stop_assignments_in_frame_rel_structure import (
    VehicleJourneyStopAssignmentsInFrameRelStructure,
)
from .vehicle_mode_enumeration import VehicleModeEnumeration
from .vehicle_type_ref import VehicleTypeRef
from .vehicle_types_in_frame_rel_structure import (
    VehicleTypesInFrameRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimetableVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Timetable_VersionFrameStructure"

    vehicle_modes: Sequence[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    headway_service: None | bool = field(
        default=None,
        metadata={
            "name": "HeadwayService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    monitored: None | bool = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    network_view: None | NetworkView = field(
        default=None,
        metadata={
            "name": "NetworkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_view: None | LineView = field(
        default=None,
        metadata={
            "name": "LineView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_view: None | OperatorView = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_calendar_frame_ref: None | ServiceCalendarFrameRef = field(
        default=None,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_mode: None | VehicleModeEnumeration = field(
        default=None,
        metadata={
            "name": "DefaultMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_accounting_ref: None | JourneyAccountingRef = field(
        default=None,
        metadata={
            "name": "JourneyAccountingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_times: None | ContainedAvailabilityConditionsRelStructure = field(
        default=None,
        metadata={
            "name": "bookingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: None | AccessibilityAssessment = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_type_ref_or_vehicle_type_ref: (
        None
        | SimpleVehicleTypeRef
        | CompoundTrainRef
        | TrainRef
        | VehicleTypeRef
        | TransportTypeRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    time_demand_types: None | TimeDemandTypesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_assignments: (
        None | TimeDemandTypeAssignmentsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "timeDemandTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_link_groups: None | GroupOfLinksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timingLinkGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journeys: None | JourneysInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency_groups: None | FrequencyGroupsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "frequencyGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_services: None | GroupsOfServicesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_numbers: None | TrainNumbersInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_couples: None | JourneyPartCouplesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "journeyPartCouples",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    coupled_journeys: None | CoupledJourneysInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "coupledJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_sets: None | ServiceFacilitySetsInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "serviceFacilitySets",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    types_of_service: None | TypesOfServiceInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "typesOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_service_properties: (
        None | FlexibleServicePropertiesInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "flexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journey_stop_assignments: (
        None | VehicleJourneyStopAssignmentsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "vehicleJourneyStopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notices: None | NoticesInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: None | NoticeAssignmentsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_meetings: None | JourneyMeetingsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "journeyMeetings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_interchanges: None | JourneyInterchangesInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "journeyInterchanges",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    default_interchanges: None | DefaultInterchangesInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "defaultInterchanges",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    interchange_rules: None | InterchangeRulesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "interchangeRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_types: None | VehicleTypesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_accountings: None | JourneyAccountingsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "journeyAccountings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
