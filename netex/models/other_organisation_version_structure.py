from dataclasses import dataclass, field
from typing import Optional

from .organisation_version_structure import OrganisationVersionStructure
from .postal_address_version_structure import PostalAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OtherOrganisationVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "OtherOrganisation_VersionStructure"

    address: Optional[PostalAddressVersionStructure] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
