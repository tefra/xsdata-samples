from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from .alternative_texts_rel_structure import VersionedChildStructure
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef

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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
                {
                    "name": "StartTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
