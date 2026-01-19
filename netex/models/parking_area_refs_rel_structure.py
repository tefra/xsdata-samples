from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_area_ref import ParkingAreaRef
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingAreaRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "parkingAreaRefs_RelStructure"

    parking_area_ref: Sequence[
        VehiclePoolingParkingAreaRef
        | VehicleSharingParkingAreaRef
        | TaxiParkingAreaRef
        | ParkingAreaRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
