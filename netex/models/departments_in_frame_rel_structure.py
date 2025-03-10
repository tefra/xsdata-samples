from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .department import Department

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DepartmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "departmentsInFrame_RelStructure"

    department: Iterable[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
