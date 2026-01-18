from __future__ import annotations

from dataclasses import dataclass, field

from .log_entry_version_structure import LogEntryVersionStructure
from .monitored_vehicle_sharing_parking_bay_ref import (
    MonitoredVehicleSharingParkingBayRef,
)
from .parking_bay_ref import ParkingBayRef
from .parking_bay_status_enumeration import ParkingBayStatusEnumeration
from .parking_bay_status_ref import ParkingBayStatusRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayConditionVersionStructure(LogEntryVersionStructure):
    class Meta:
        name = "ParkingBayCondition_VersionStructure"

    parking_bay_ref_or_vehicle_sharing_parking_bay_ref: (
        VehiclePoolingParkingBayRef
        | MonitoredVehicleSharingParkingBayRef
        | VehicleSharingParkingBayRef
        | ParkingBayRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingBayRef",
                    "type": VehiclePoolingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBayRef",
                    "type": MonitoredVehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBayRef",
                    "type": VehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayRef",
                    "type": ParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
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
