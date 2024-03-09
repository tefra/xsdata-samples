from dataclasses import dataclass

from .transport_organisation_version_structure import (
    TransportOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatorVersionStructure(TransportOrganisationVersionStructure):
    class Meta:
        name = "Operator_VersionStructure"
