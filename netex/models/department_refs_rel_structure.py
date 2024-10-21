from collections.abc import Iterable
from dataclasses import dataclass, field

from .department_ref import DepartmentRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DepartmentRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "departmentRefs_RelStructure"

    department_ref: Iterable[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
