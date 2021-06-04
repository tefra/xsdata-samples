from dataclasses import dataclass
from netex.models.vehicle_stopping_position_ref_structure import VehicleStoppingPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPositionRef(VehicleStoppingPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
