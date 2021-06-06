from dataclasses import dataclass, field
from typing import Optional
from .country_ref import CountryRef
from .organisation_version_structure import OrganisationVersionStructure
from .postal_address_version_structure import PostalAddressVersionStructure
from .type_of_organisation_refs_rel_structure import TypeOfOrganisationRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AuthorityVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "Authority_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    address: Optional[PostalAddressVersionStructure] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_types: Optional[TypeOfOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "authorityTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
