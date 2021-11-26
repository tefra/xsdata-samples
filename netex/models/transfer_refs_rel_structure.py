from dataclasses import dataclass, field
from typing import List
from .access_ref import AccessRef
from .connection_ref import ConnectionRef
from .default_connection_ref import DefaultConnectionRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .site_connection_ref import SiteConnectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "transferRefs_RelStructure"

    default_connection_ref: List[DefaultConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "DefaultConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_connection_ref: List[SiteConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connection_ref: List[ConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_ref: List[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
