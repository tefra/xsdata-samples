from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .department import Department
from .department_ref import DepartmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DepartmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "departments_RelStructure"

    department_ref: List[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department: List[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )