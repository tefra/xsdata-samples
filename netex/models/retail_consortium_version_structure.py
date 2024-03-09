from dataclasses import dataclass, field
from typing import Optional

from .blacklist_refs_rel_structure import BlacklistRefsRelStructure
from .organisation_refs_rel_structure import OrganisationRefsRelStructure
from .organisation_version_structure import OrganisationVersionStructure
from .postal_address import PostalAddress
from .retail_devices_rel_structure import RetailDevicesRelStructure
from .whitelist_refs_rel_structure import WhitelistRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailConsortiumVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "RetailConsortium_VersionStructure"

    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blacklist_refs: Optional[BlacklistRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "blacklistRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    whitelist_refs: Optional[WhitelistRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "whitelistRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_devices: Optional[RetailDevicesRelStructure] = field(
        default=None,
        metadata={
            "name": "retailDevices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
