from dataclasses import dataclass

from .garage_version_structure import GarageVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Garage(GarageVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
