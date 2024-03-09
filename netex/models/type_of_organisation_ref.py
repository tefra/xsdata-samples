from dataclasses import dataclass

from .type_of_organisation_ref_structure import TypeOfOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfOrganisationRef(TypeOfOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
