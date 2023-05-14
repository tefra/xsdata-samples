from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .blacklist_ref import BlacklistRef
from .multilingual_string import MultilingualString
from .whitelist_ref import WhitelistRef

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
    whitelist_ref_or_blacklist_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
