from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .group_of_operators_ref import GroupOfOperatorsRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfOperatorsRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupsOfOperatorsRefs_RelStructure"

    group_of_operators_ref: Sequence[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
