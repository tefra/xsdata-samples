from dataclasses import dataclass, field
from typing import Optional

from .transport_organisation_version_structure import (
    TransportOrganisationVersionStructure,
)
from .type_of_organisation_refs_rel_structure import (
    TypeOfOrganisationRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AuthorityVersionStructure(TransportOrganisationVersionStructure):
    class Meta:
        name = "Authority_VersionStructure"

    authority_types: Optional[TypeOfOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "authorityTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
