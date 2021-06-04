from dataclasses import dataclass
from netex.models.organisation_version_structure import OrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOrganisation(OrganisationVersionStructure):
    class Meta:
        name = "TransportOrganisation_"
        namespace = "http://www.netex.org.uk/netex"
