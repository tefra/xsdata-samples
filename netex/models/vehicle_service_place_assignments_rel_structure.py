from dataclasses import dataclass, field
from typing import List, Union
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .taxi_service_place_assignment import TaxiServicePlaceAssignment
from .vehicle_pooling_place_assignment import VehiclePoolingPlaceAssignment
from .vehicle_sharing_place_assignment import VehicleSharingPlaceAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePlaceAssignmentsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "vehicleServicePlaceAssignments_RelStructure"

    vehicle_sharing_place_assignment_or_vehicle_pooling_place_assignment_or_taxi_service_place_assignment: List[
        Union[
            VehicleSharingPlaceAssignment,
            VehiclePoolingPlaceAssignment,
            TaxiServicePlaceAssignment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleSharingPlaceAssignment",
                    "type": VehicleSharingPlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingPlaceAssignment",
                    "type": VehiclePoolingPlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServicePlaceAssignment",
                    "type": TaxiServicePlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
