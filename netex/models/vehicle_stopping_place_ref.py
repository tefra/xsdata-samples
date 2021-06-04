from dataclasses import dataclass
from netex.models.vehicle_stopping_place_ref_structure import VehicleStoppingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPlaceRef(VehicleStoppingPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
