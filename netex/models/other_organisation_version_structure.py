from __future__ import annotations

from dataclasses import dataclass, field

from .organisation_version_structure import OrganisationVersionStructure
from .postal_address_version_structure import PostalAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherOrganisationVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "OtherOrganisation_VersionStructure"

    address: None | PostalAddressVersionStructure = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
