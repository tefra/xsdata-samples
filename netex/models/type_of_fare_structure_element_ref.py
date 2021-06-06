from dataclasses import dataclass
from .type_of_fare_structure_element_ref_structure import TypeOfFareStructureElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareStructureElementRef(TypeOfFareStructureElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
