from __future__ import annotations

from dataclasses import dataclass

from .type_of_parking_value_structure import TypeOfParkingValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfParking(TypeOfParkingValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
