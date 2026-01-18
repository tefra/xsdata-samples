from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration, XmlTime

from .headway_interval_structure import HeadwayIntervalStructure
from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimetabledPassingTimeViewStructure(PassingTimeViewStructure):
    class Meta:
        name = "TimetabledPassingTime_ViewStructure"

    arrival_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    arrival_day_offset: None | int = field(
        default=None,
        metadata={
            "name": "ArrivalDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: None | int = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    waiting_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "WaitingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headway: None | HeadwayIntervalStructure = field(
        default=None,
        metadata={
            "name": "Headway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
