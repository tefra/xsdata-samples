from dataclasses import dataclass, field
from typing import List
from .fare_scheduled_stop_point import FareScheduledStopPoint
from .frame_containment_structure import FrameContainmentStructure
from .scheduled_stop_point import ScheduledStopPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareScheduledStopPointsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareScheduledStopPointsInFrame_RelStructure"

    scheduled_stop_point: List[ScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point: List[FareScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
