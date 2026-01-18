from dataclasses import dataclass, field
from typing import Optional, Union

from .car_pooling_service_ref import CarPoolingServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .mobility_service_constraint_zone_ref import (
    MobilityServiceConstraintZoneRef,
)
from .online_service_ref import OnlineServiceRef
from .parking_component_refs_rel_structure import (
    ParkingComponentRefsRelStructure,
)
from .parking_ref import ParkingRef
from .taxi_service_ref import TaxiServiceRef
from .vehicle_refs_rel_structure import VehicleRefsRelStructure
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PoolOfVehiclesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "PoolOfVehicles_VersionStructure"

    mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref: OnlineServiceRef | VehicleRentalServiceRef | VehicleSharingServiceRef | ChauffeuredVehicleServiceRef | TaxiServiceRef | CarPoolingServiceRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
    mobility_service_constraint_zone_ref: MobilityServiceConstraintZoneRef | None = field(
        default=None,
        metadata={
            "name": "MobilityServiceConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_ref: ParkingRef | None = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_components: ParkingComponentRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "parkingComponents",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    must_return_to_same_bay: bool | None = field(
        default=None,
        metadata={
            "name": "MustReturnToSameBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicles: VehicleRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
