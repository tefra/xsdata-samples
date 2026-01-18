from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_proof_ref import TypeOfProofRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfProofRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typesOfProofRefs_RelStructure"

    type_of_proof_ref: Iterable[TypeOfProofRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProofRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
