from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from .dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObservedPassingTimeVersionedChildStructure(DatedPassingTimeVersionedChildStructure):
    class Meta:
        name = "ObservedPassingTime_VersionedChildStructure"

    choice_2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualDepartureTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualNonstopPassingTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
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
