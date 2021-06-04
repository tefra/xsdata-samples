from dataclasses import dataclass
from netex.models.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFeatureValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfFeature_ValueStructure"
