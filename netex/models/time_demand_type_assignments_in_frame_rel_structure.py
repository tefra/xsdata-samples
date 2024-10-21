from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .time_demand_type_assignment import TimeDemandTypeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypeAssignmentsInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "timeDemandTypeAssignmentsInFrame_RelStructure"

    time_demand_type_assignment: Iterable[TimeDemandTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
