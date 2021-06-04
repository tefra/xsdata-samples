from dataclasses import dataclass
from netex.models.parking_component_version_structure import ParkingComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingComponent(ParkingComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
