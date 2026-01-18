from __future__ import annotations

from dataclasses import dataclass

from .parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GaragePointVersionStructure(ParkingPointVersionStructure):
    class Meta:
        name = "GaragePoint_VersionStructure"
