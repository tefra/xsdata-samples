from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.models.border_point_ref import BorderPointRef
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.garage_point_ref import GaragePointRef
from netex.models.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from netex.models.parking_point_ref import ParkingPointRef
from netex.models.relief_point_ref import ReliefPointRef
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyWaitTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    class Meta:
        name = "JourneyWaitTime_VersionedChildStructure"

    border_point_ref: List[BorderPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    scheduled_stop_point_ref: List[ScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    garage_point_ref: List[GaragePointRef] = field(
        default_factory=list,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    parking_point_ref: List[ParkingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    relief_point_ref: List[ReliefPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    timing_point_ref: Optional[TimingPointRef] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
