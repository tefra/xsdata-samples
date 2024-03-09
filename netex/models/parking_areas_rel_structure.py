from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_area_1 import ParkingArea1
from .parking_area_ref import ParkingAreaRef
from .taxi_parking_area import TaxiParkingArea
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .vehicle_pooling_parking_area import VehiclePoolingParkingArea
from .vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from .vehicle_sharing_parking_area import VehicleSharingParkingArea
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingAreasRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingAreas_RelStructure"

    parking_area_ref_or_parking_area: List[
        Union[
            VehiclePoolingParkingAreaRef,
            VehicleSharingParkingAreaRef,
            TaxiParkingAreaRef,
            ParkingAreaRef,
            VehiclePoolingParkingArea,
            VehicleSharingParkingArea,
            TaxiParkingArea,
            ParkingArea1,
        ]
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
                {
                    "name": "VehiclePoolingParkingArea",
                    "type": VehiclePoolingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingArea",
                    "type": VehicleSharingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingArea",
                    "type": TaxiParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
