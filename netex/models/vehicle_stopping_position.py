from dataclasses import dataclass
from netex.models.vehicle_stopping_position_version_structure import VehicleStoppingPositionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPosition(VehicleStoppingPositionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
