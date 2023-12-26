from dataclasses import dataclass
from .serviced_organisation_version_structure import (
    ServicedOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicedOrganisation(ServicedOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
