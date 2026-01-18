from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMachineReadabilityRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TypeOfMachineReadabilityRefs_RelStructure"

    type_of_machine_readability_ref: Iterable[TypeOfMachineReadabilityRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "TypeOfMachineReadabilityRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
