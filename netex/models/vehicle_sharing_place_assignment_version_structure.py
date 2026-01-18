from __future__ import annotations

from dataclasses import dataclass, field

from .car_pooling_service_ref import CarPoolingServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .monitored_vehicle_sharing_parking_bay_ref import (
    MonitoredVehicleSharingParkingBayRef,
)
from .parking_bay_ref import ParkingBayRef
from .taxi_service_ref import TaxiServiceRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_service_place_assignment_version_structure import (
    VehicleServicePlaceAssignmentVersionStructure,
)
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingPlaceAssignmentVersionStructure(
    VehicleServicePlaceAssignmentVersionStructure
):
    class Meta:
        name = "VehicleSharingPlaceAssignment_VersionStructure"

    common_vehicle_service_ref_or_vehicle_pooling_service_ref: (
        VehicleRentalServiceRef
        | VehicleSharingServiceRef
        | ChauffeuredVehicleServiceRef
        | TaxiServiceRef
        | CarPoolingServiceRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_sharing_parking_area_ref: VehicleSharingParkingAreaRef | None = (
        field(
            default=None,
            metadata={
                "name": "VehicleSharingParkingAreaRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
    )
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
