from dataclasses import dataclass, field
from typing import List
from netex.models.department_ref import DepartmentRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DepartmentRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "departmentRefs_RelStructure"

    department_ref: List[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
