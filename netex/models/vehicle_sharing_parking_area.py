from dataclasses import dataclass

from .vehicle_sharing_parking_area_version_structure import (
    VehicleSharingParkingAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingParkingArea(VehicleSharingParkingAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
