from dataclasses import dataclass

from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfOrganisationValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfOrganisation_ValueStructure"
