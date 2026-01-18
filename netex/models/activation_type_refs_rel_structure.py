from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "activationTypeRefs_RelStructure"

    type_of_activation_ref: Iterable[TypeOfActivationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
