from __future__ import annotations

from dataclasses import dataclass

from .parking_point_ref_structure import ParkingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointRefStructure(ParkingPointRefStructure):
    pass
