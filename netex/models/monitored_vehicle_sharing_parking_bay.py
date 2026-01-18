from __future__ import annotations

from dataclasses import dataclass

from .monitored_vehicle_sharing_parking_bay_version_structure import (
    MonitoredVehicleSharingParkingBayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonitoredVehicleSharingParkingBay(
    MonitoredVehicleSharingParkingBayVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
