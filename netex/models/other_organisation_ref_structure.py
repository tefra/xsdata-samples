from dataclasses import dataclass
from .organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OtherOrganisationRefStructure(OrganisationRefStructure):
    pass
