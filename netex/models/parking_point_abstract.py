from __future__ import annotations

from dataclasses import dataclass

from .relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPointAbstract(ReliefPointVersionStructure):
    class Meta:
        name = "ParkingPoint_"
        namespace = "http://www.netex.org.uk/netex"
