from dataclasses import dataclass
from netex.models.organisation_version_structure import OrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Organisation1(OrganisationVersionStructure):
    class Meta:
        name = "Organisation"
        namespace = "http://www.netex.org.uk/netex"
