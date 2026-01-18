from dataclasses import dataclass, field

from .parking_bay_status_enumeration import ParkingBayStatusEnumeration
from .parking_bay_status_ref import ParkingBayStatusRef
from .vehicle_sharing_parking_bay_version_structure import (
    VehicleSharingParkingBayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonitoredVehicleSharingParkingBayVersionStructure(
    VehicleSharingParkingBayVersionStructure
):
    class Meta:
        name = "MonitoredVehicleSharingParkingBay_VersionStructure"

    status: ParkingBayStatusEnumeration | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_bay_status_ref: ParkingBayStatusRef | None = field(
        default=None,
        metadata={
            "name": "ParkingBayStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
