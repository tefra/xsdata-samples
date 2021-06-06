from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_security_list_ref import TypeOfSecurityListRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfSecurityListRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfSecurityListRefs_RelStructure"

    type_of_security_list_ref: List[TypeOfSecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
