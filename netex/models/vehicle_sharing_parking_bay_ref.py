from dataclasses import dataclass
from .vehicle_sharing_parking_bay_ref_structure import (
    VehicleSharingParkingBayRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingParkingBayRef(VehicleSharingParkingBayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
