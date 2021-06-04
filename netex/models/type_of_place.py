from dataclasses import dataclass
from netex.models.type_of_place_value_structure import TypeOfPlaceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPlace(TypeOfPlaceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
