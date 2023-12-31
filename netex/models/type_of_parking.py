from dataclasses import dataclass
from .type_of_parking_value_structure import TypeOfParkingValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfParking(TypeOfParkingValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
