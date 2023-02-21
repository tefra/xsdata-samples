from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from .dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TargetPassingTimeVersionedChildStructure(DatedPassingTimeVersionedChildStructure):
    class Meta:
        name = "TargetPassingTime_VersionedChildStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AimedArrivalTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedDepartureTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedNonstopPassingTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 7,
        }
    )
    aimed_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "AimedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
