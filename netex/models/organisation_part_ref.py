from dataclasses import dataclass
from netex.models.organisation_part_ref_structure import OrganisationPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationPartRef(OrganisationPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
