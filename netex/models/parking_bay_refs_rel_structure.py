from dataclasses import dataclass, field
from typing import List, Union

from .monitored_vehicle_sharing_parking_bay_ref import (
    MonitoredVehicleSharingParkingBayRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_bay_ref import ParkingBayRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "parkingBayRefs_RelStructure"

    parking_bay_ref_or_vehicle_sharing_parking_bay_ref: List[
        Union[
            VehiclePoolingParkingBayRef,
            MonitoredVehicleSharingParkingBayRef,
            VehicleSharingParkingBayRef,
            ParkingBayRef,
        ]
    ] = field(
        default_factory=list,
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
