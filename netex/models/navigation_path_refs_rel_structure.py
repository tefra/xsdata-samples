from dataclasses import dataclass, field
from typing import List
from .navigation_path_ref import NavigationPathRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "navigationPathRefs_RelStructure"

    navigation_path_ref: List[NavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
