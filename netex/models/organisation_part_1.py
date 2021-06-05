from dataclasses import dataclass
from netex.models.organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationPart1(OrganisationPartVersionStructure):
    class Meta:
        name = "OrganisationPart"
        namespace = "http://www.netex.org.uk/netex"
