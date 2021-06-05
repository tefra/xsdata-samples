from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.models.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.models.direction_ref import DirectionRef
from netex.models.display_assignment_type_enumeration import DisplayAssignmentTypeEnumeration
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.journey_pattern_ref import JourneyPatternRef
from netex.models.line_ref import LineRef
from netex.models.logical_display_ref import LogicalDisplayRef
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.service_pattern_ref import ServicePatternRef

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
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_pattern_ref: List[ServicePatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    dead_run_journey_pattern_ref: List[DeadRunJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    display_assignment_type: Optional[DisplayAssignmentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DisplayAssignmentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_journeys_to_show: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfJourneysToShow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    display_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
