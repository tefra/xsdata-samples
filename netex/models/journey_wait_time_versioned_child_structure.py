from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDuration
from .border_point_ref import BorderPointRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from .parking_point_ref import ParkingPointRef
from .relief_point_ref import ReliefPointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyWaitTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    class Meta:
        name = "JourneyWaitTime_VersionedChildStructure"

    choice: List[object] = field(
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
                },
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
            ),
            "max_occurs": 16,
        }
    )
