from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from .dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TargetPassingTimeVersionedChildStructure(DatedPassingTimeVersionedChildStructure):
    class Meta:
        name = "TargetPassingTime_VersionedChildStructure"

    aimed_arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "ArrivalDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    aimed_departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    aimed_waiting_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AimedWaitingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    aimed_nonstop_passing_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "AimedNonstopPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passing_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "PassingDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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