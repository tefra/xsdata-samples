from dataclasses import dataclass

from .garage_ref_structure import GarageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GarageRef(GarageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
