from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.blacklist_ref import BlacklistRef
from netex.models.multilingual_string import MultilingualString
from netex.models.security_list_ref import SecurityListRef
from netex.models.whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListingVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "SecurityListing_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    whitelist_ref: List[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    security_list_ref: Optional[SecurityListRef] = field(
        default=None,
        metadata={
            "name": "SecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
