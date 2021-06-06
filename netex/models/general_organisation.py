from dataclasses import dataclass
from .general_organisation_version_structure import GeneralOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralOrganisation(GeneralOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
