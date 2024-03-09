from dataclasses import dataclass

from .serviced_organisation_ref_structure import (
    ServicedOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicedOrganisationRef(ServicedOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
