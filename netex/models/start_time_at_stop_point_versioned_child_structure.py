from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.fare_demand_factor_ref import FareDemandFactorRef
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StartTimeAtStopPointVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "StartTimeAtStopPoint_VersionedChildStructure"

    fare_demand_factor_ref: Optional[FareDemandFactorRef] = field(
        default=None,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
