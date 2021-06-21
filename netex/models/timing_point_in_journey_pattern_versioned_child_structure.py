from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDuration
from .border_point_ref import BorderPointRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from .journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .parking_point_ref import ParkingPointRef
from .point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from .relief_point_ref import ReliefPointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .timing_link_ref_structure import TimingLinkRefStructure
from .timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointInJourneyPatternVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "TimingPointInJourneyPattern_VersionedChildStructure"

    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
                {
                    "name": "OnwardTimingLinkRef",
                    "type": TimingLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IsWaitPoint",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "waitTimes",
                    "type": JourneyPatternWaitTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "headways",
                    "type": JourneyPatternHeadwaysRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 6,
            "max_occurs": 16,
        }
    )
