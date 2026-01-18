from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from .accessibility_assessment import AccessibilityAssessment
from .check_constraint import CheckConstraint
from .duty_part_ref import DutyPartRef
from .dynamic_stop_assignment import DynamicStopAssignment
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .interchange_rules_rel_structure import InterchangeRulesRelStructure
from .journey_meeting_views_rel_structure import (
    JourneyMeetingViewsRelStructure,
)
from .journey_part_ref import JourneyPartRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .quay_assignment_view import QuayAssignmentView
from .service_journey_interchanges_rel_structure import (
    ServiceJourneyInterchangesRelStructure,
)
from .time_demand_type_ref import TimeDemandTypeRef
from .timeband_ref import TimebandRef
from .vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ArrivalStructure:
    time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_offset: int | None = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_alighting: bool | None = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_flexible: bool | None = field(
        default=None,
        metadata={
            "name": "IsFlexible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_ref: JourneyPartRef | None = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_meetings: JourneyMeetingViewsRelStructure | None = field(
        default=None,
        metadata={
            "name": "journeyMeetings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    interchanges: ServiceJourneyInterchangesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    interchange_rules: InterchangeRulesRelStructure | None = field(
        default=None,
        metadata={
            "name": "interchangeRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref_or_timeband_ref: (
        TimeDemandTypeRef | TimebandRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    duty_part_ref: DutyPartRef | None = field(
        default=None,
        metadata={
            "name": "DutyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: (
        VehicleJourneyStopAssignmentRef
        | DynamicStopAssignmentRef
        | PassengerStopAssignmentRef
        | QuayAssignmentView
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayAssignmentView",
                    "type": QuayAssignmentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    dynamic_stop_assignment: DynamicStopAssignment | None = field(
        default=None,
        metadata={
            "name": "DynamicStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: AccessibilityAssessment | None = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraint: CheckConstraint | None = field(
        default=None,
        metadata={
            "name": "CheckConstraint",
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
