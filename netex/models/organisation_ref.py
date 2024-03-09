from dataclasses import dataclass

from .organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationRef(OrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
