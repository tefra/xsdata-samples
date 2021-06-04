from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.common_version_frame_structure import CommonVersionFrameStructure
from netex.models.compound_train_ref import CompoundTrainRef
from netex.models.contained_availability_conditions_rel_structure import ContainedAvailabilityConditionsRelStructure
from netex.models.coupled_journeys_in_frame_rel_structure import CoupledJourneysInFrameRelStructure
from netex.models.default_interchangse_in_frame_rel_structure import DefaultInterchangseInFrameRelStructure
from netex.models.flexible_service_properties_in_frame_rel_structure import FlexibleServicePropertiesInFrameRelStructure
from netex.models.frequency_groups_in_frame_rel_structure import FrequencyGroupsInFrameRelStructure
from netex.models.group_of_links_in_frame_rel_structure import GroupOfLinksInFrameRelStructure
from netex.models.groups_of_services_in_frame_rel_structure import GroupsOfServicesInFrameRelStructure
from netex.models.interchange_rules_in_frame_rel_structure import InterchangeRulesInFrameRelStructure
from netex.models.journey_accounting_ref import JourneyAccountingRef
from netex.models.journey_accountings_in_frame_rel_structure import JourneyAccountingsInFrameRelStructure
from netex.models.journey_interchanges_in_frame_rel_structure import JourneyInterchangesInFrameRelStructure
from netex.models.journey_meetings_in_frame_rel_structure import JourneyMeetingsInFrameRelStructure
from netex.models.journey_part_couples_in_frame_rel_structure import JourneyPartCouplesInFrameRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line_view import LineView
from netex.models.network_view import NetworkView
from netex.models.notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.operator_view import OperatorView
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.models.time_demand_type_assignments_in_frame_rel_structure import TimeDemandTypeAssignmentsInFrameRelStructure
from netex.models.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.models.train_numbers_in_frame_rel_structure import TrainNumbersInFrameRelStructure
from netex.models.train_ref import TrainRef
from netex.models.types_of_service_in_frame_rel_structure import TypesOfServiceInFrameRelStructure
from netex.models.vehicle_journey_stop_assignments_in_frame_rel_structure import VehicleJourneyStopAssignmentsInFrameRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.vehicle_type_ref import VehicleTypeRef
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure

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
    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_type_ref: Optional[VehicleTypeRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_types: Optional[TimeDemandTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_assignments: Optional[TimeDemandTypeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_groups: Optional[GroupOfLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timingLinkGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journeys: Optional[JourneysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_groups: Optional[FrequencyGroupsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "frequencyGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_services: Optional[GroupsOfServicesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_numbers: Optional[TrainNumbersInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couples: Optional[JourneyPartCouplesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPartCouples",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    coupled_journeys: Optional[CoupledJourneysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "coupledJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_sets: Optional[ServiceFacilitySetsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "serviceFacilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_service: Optional[TypesOfServiceInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_properties: Optional[FlexibleServicePropertiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "flexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_stop_assignments: Optional[VehicleJourneyStopAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleJourneyStopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notices: Optional[NoticesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_meetings: Optional[JourneyMeetingsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyMeetings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_interchanges: Optional[JourneyInterchangesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_interchanges: Optional[DefaultInterchangseInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "defaultInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rules: Optional[InterchangeRulesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "interchangeRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_types: Optional[VehicleTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accountings: Optional[JourneyAccountingsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyAccountings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
