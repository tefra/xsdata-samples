from dataclasses import dataclass
from .all_transport_organisations_ref_structure import (
    AllTransportOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllAuthoritiesRef(AllTransportOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
