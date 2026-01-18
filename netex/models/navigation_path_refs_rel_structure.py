from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .navigation_path_ref import NavigationPathRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "navigationPathRefs_RelStructure"

    navigation_path_ref: Iterable[NavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
