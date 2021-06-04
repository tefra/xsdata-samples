from dataclasses import dataclass, field
from typing import List
from netex.models.access_ref import AccessRef
from netex.models.connection_ref import ConnectionRef
from netex.models.default_connection_ref import DefaultConnectionRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.site_connection_ref import SiteConnectionRef
from netex.models.transfer_ref import TransferRef

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
            "min_occurs": 1,
        }
    )
    site_connection_ref: List[SiteConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    connection_ref: List[ConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_ref: List[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transfer_ref: List[TransferRef] = field(
        default_factory=list,
        metadata={
            "name": "TransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
