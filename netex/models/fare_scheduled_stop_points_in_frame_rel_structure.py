from dataclasses import dataclass, field
from typing import List, Union

from .fare_scheduled_stop_point import FareScheduledStopPoint
from .frame_containment_structure import FrameContainmentStructure
from .scheduled_stop_point import ScheduledStopPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareScheduledStopPointsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareScheduledStopPointsInFrame_RelStructure"

    scheduled_stop_point_or_fare_scheduled_stop_point: List[
        Union[ScheduledStopPoint, FareScheduledStopPoint]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
