from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfAccessRightAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "TypeOfAccessRightAssignmentRefs_RelStructure"

    type_of_access_right_assignment_ref: List[
        TypeOfAccessRightAssignmentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
