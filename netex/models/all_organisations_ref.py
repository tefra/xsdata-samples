from dataclasses import dataclass
from netex.models.all_organisations_ref_structure import AllOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllOrganisationsRef(AllOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
