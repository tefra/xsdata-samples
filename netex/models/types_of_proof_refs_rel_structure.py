from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_proof_ref import TypeOfProofRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfProofRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typesOfProofRefs_RelStructure"

    type_of_proof_ref: List[TypeOfProofRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProofRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
