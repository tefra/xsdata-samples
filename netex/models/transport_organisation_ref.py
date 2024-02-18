from dataclasses import dataclass
from .transport_organisation_ref_structure import (
    TransportOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOrganisationRef(TransportOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
