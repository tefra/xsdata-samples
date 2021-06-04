from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.models.dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure
from netex.models.headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObservedPassingTimeVersionedChildStructure(DatedPassingTimeVersionedChildStructure):
    class Meta:
        name = "ObservedPassingTime_VersionedChildStructure"

    actual_arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
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
    actual_departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTime",
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
    actual_waiting_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ActualWaitingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    actual_nonstop_passing_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ActualNonstopPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passing_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "PassingTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    actual_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "ActualHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
