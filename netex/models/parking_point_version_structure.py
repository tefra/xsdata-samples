from dataclasses import dataclass

from .relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPointVersionStructure(ReliefPointVersionStructure):
    class Meta:
        name = "ParkingPoint_VersionStructure"
