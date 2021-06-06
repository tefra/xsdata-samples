from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .open_transport_mode_ref import OpenTransportModeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OpenTransportModeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "openTransportModeRefs_RelStructure"

    open_transport_mode_ref: List[OpenTransportModeRef] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
