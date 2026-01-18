from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .garage_ref import GarageRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GarageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "garageRefs_RelStructure"

    garage_ref: Iterable[GarageRef] = field(
        default_factory=list,
        metadata={
            "name": "GarageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
