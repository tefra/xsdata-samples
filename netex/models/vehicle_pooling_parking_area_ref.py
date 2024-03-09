from dataclasses import dataclass

from .vehicle_pooling_parking_area_ref_structure import (
    VehiclePoolingParkingAreaRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingParkingAreaRef(VehiclePoolingParkingAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
