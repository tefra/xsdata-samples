from dataclasses import dataclass
from netex.models.other_organisation_ref_structure import OtherOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OtherOrganisationRef(OtherOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
