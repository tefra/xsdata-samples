from dataclasses import dataclass
from .all_public_transport_organisations_ref_structure import (
    AllPublicTransportOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllAuthoritiesRefStructure(AllPublicTransportOrganisationsRefStructure):
    pass
