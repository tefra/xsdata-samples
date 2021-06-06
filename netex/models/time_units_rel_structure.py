from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .time_unit import TimeUnit
from .time_unit_ref import TimeUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeUnitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timeUnits_RelStructure"

    time_unit_ref: List[TimeUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit: List[TimeUnit] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
