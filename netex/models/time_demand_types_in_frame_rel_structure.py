from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .time_demand_type import TimeDemandType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timeDemandTypesInFrame_RelStructure"

    time_demand_type: List[TimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
