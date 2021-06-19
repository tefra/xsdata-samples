from dataclasses import dataclass, field
from typing import List, Optional
from .accessibility_assessment import AccessibilityAssessment
from .common_version_frame_structure import CommonVersionFrameStructure
from .compound_train_ref import CompoundTrainRef
from .contained_availability_conditions_rel_structure import ContainedAvailabilityConditionsRelStructure
from .coupled_journeys_in_frame_rel_structure import CoupledJourneysInFrameRelStructure
from .default_interchangse_in_frame_rel_structure import DefaultInterchangseInFrameRelStructure
from .flexible_service_properties_in_frame_rel_structure import FlexibleServicePropertiesInFrameRelStructure
from .frequency_groups_in_frame_rel_structure import FrequencyGroupsInFrameRelStructure
from .group_of_links_in_frame_rel_structure import GroupOfLinksInFrameRelStructure
from .groups_of_services_in_frame_rel_structure import GroupsOfServicesInFrameRelStructure
from .interchange_rules_in_frame_rel_structure import InterchangeRulesInFrameRelStructure
from .journey_accounting_ref import JourneyAccountingRef
from .journey_accountings_in_frame_rel_structure import JourneyAccountingsInFrameRelStructure
from .journey_interchanges_in_frame_rel_structure import JourneyInterchangesInFrameRelStructure
from .journey_meetings_in_frame_rel_structure import JourneyMeetingsInFrameRelStructure
from .journey_part_couples_in_frame_rel_structure import JourneyPartCouplesInFrameRelStructure
from .journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from .line_view import LineView
from .network_view import NetworkView
from .notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from .notices_in_frame_rel_structure import NoticesInFrameRelStructure
from .operator_view import OperatorView
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from .time_demand_type_assignments_in_frame_rel_structure import TimeDemandTypeAssignmentsInFrameRelStructure
from .time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from .train_numbers_in_frame_rel_structure import TrainNumbersInFrameRelStructure
from .train_ref import TrainRef
from .types_of_service_in_frame_rel_structure import TypesOfServiceInFrameRelStructure
from .vehicle_journey_stop_assignments_in_frame_rel_structure import VehicleJourneyStopAssignmentsInFrameRelStructure
from .vehicle_mode_enumeration import VehicleModeEnumeration
from .vehicle_type_ref import VehicleTypeRef
from .vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimetableVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Timetable_VersionFrameStructure"

    vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_view: Optional[NetworkView] = field(
        default=None,
        metadata={
            "name": "NetworkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_view: Optional[LineView] = field(
        default=None,
        metadata={
            "name": "LineView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_view: Optional[OperatorView] = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame_ref: Optional[ServiceCalendarFrameRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "DefaultMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accounting_ref: Optional[JourneyAccountingRef] = field(
        default=None,
        metadata={
            "name": "JourneyAccountingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_times: Optional[ContainedAvailabilityConditionsRelStructure] = field(
        default=None,
        metadata={
            "name": "bookingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
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
                    "name": "timeDemandTypes",
                    "type": TimeDemandTypesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeDemandTypeAssignments",
                    "type": TimeDemandTypeAssignmentsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timingLinkGroups",
                    "type": GroupOfLinksInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "vehicleJourneys",
                    "type": JourneysInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "frequencyGroups",
                    "type": FrequencyGroupsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfServices",
                    "type": GroupsOfServicesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "trainNumbers",
                    "type": TrainNumbersInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyPartCouples",
                    "type": JourneyPartCouplesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "coupledJourneys",
                    "type": CoupledJourneysInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "serviceFacilitySets",
                    "type": ServiceFacilitySetsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "typesOfService",
                    "type": TypesOfServiceInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "flexibleServiceProperties",
                    "type": FlexibleServicePropertiesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "vehicleJourneyStopAssignments",
                    "type": VehicleJourneyStopAssignmentsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "notices",
                    "type": NoticesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyMeetings",
                    "type": JourneyMeetingsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyInterchanges",
                    "type": JourneyInterchangesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "defaultInterchanges",
                    "type": DefaultInterchangseInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "interchangeRules",
                    "type": InterchangeRulesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "vehicleTypes",
                    "type": VehicleTypesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyAccountings",
                    "type": JourneyAccountingsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 28,
        }
    )
