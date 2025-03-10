from collections.abc import Iterable
from dataclasses import dataclass, field

from .destination_display_ref import DestinationDisplayRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "destinationDisplayRefs_RelStructure"

    destination_display_ref: Iterable[DestinationDisplayRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
