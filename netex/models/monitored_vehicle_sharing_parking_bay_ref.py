from dataclasses import dataclass
from .monitored_vehicle_sharing_parking_bay_ref_structure import (
    MonitoredVehicleSharingParkingBayRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonitoredVehicleSharingParkingBayRef(
    MonitoredVehicleSharingParkingBayRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
