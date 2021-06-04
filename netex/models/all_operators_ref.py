from dataclasses import dataclass
from netex.models.all_transport_organisations_ref_structure import AllTransportOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllOperatorsRef(AllTransportOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
