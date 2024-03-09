from dataclasses import dataclass

from .type_of_parking_ref_structure import TypeOfParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfParkingRef(TypeOfParkingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
