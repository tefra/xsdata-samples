from dataclasses import dataclass
from netex.models.type_of_fare_structure_element_version_structure import TypeOfFareStructureElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareStructureElement(TypeOfFareStructureElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
