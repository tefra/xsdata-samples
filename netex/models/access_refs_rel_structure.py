from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_ref import AccessRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "accessRefs_RelStructure"

    access_ref: Iterable[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
