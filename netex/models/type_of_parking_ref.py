from __future__ import annotations

from dataclasses import dataclass

from .type_of_parking_ref_structure import TypeOfParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfParkingRef(TypeOfParkingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
