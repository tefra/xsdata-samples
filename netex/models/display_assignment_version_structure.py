from dataclasses import dataclass, field
from typing import Optional, Union
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .direction_ref import DirectionRef
from .display_assignment_type_enumeration import (
    DisplayAssignmentTypeEnumeration,
)
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .flexible_line_ref import FlexibleLineRef
from .journey_pattern_ref import JourneyPatternRef
from .line_ref import LineRef
from .logical_display_ref import LogicalDisplayRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "DisplayAssignment_VersionStructure"

    logical_display_ref: Optional[LogicalDisplayRef] = field(
        default=None,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_stop_point_ref: Optional[
        Union[FareScheduledStopPointRef, ScheduledStopPointRef]
    ] = field(
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
            ),
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_ref: Optional[Union[FlexibleLineRef, LineRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_pattern_ref: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    display_assignment_type: Optional[
        DisplayAssignmentTypeEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "DisplayAssignmentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_journeys_to_show: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfJourneysToShow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    display_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
