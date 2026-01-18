from dataclasses import dataclass, field
from typing import Optional, Union

from .monitored_vehicle_sharing_parking_bay_ref import (
    MonitoredVehicleSharingParkingBayRef,
)
from .parking_bay_ref import ParkingBayRef
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .taxi_service_ref import TaxiServiceRef
from .taxi_stand_ref import TaxiStandRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_service_place_assignment_version_structure import (
    VehicleServicePlaceAssignmentVersionStructure,
)
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiServicePlaceAssignmentVersionStructure(
    VehicleServicePlaceAssignmentVersionStructure
):
    class Meta:
        name = "TaxiServicePlaceAssignment_VersionStructure"

    taxi_service_ref: TaxiServiceRef | None = field(
        default=None,
        metadata={
            "name": "TaxiServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    taxi_parking_area_ref: TaxiParkingAreaRef | None = field(
        default=None,
        metadata={
            "name": "TaxiParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    taxi_stand_ref: TaxiStandRef | None = field(
        default=None,
        metadata={
            "name": "TaxiStandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_bay_ref_or_vehicle_sharing_parking_bay_ref: VehiclePoolingParkingBayRef | MonitoredVehicleSharingParkingBayRef | VehicleSharingParkingBayRef | ParkingBayRef | None = field(
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
