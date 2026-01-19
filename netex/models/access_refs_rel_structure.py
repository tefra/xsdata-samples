from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .access_ref import AccessRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "accessRefs_RelStructure"

    access_ref: Sequence[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
