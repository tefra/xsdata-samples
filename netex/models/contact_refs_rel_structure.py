from dataclasses import dataclass, field
from typing import List

from .contact_ref import ContactRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContactRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "contactRefs_RelStructure"

    contact_ref: List[ContactRef] = field(
        default_factory=list,
        metadata={
            "name": "ContactRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
