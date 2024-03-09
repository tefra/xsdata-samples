from dataclasses import dataclass, field
from typing import Optional, Union

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .taxi_service_place_assignment_ref import TaxiServicePlaceAssignmentRef
from .vehicle_pooling_place_assignment_ref import (
    VehiclePoolingPlaceAssignmentRef,
)
from .vehicle_service_place_assignment_ref import (
    VehicleServicePlaceAssignmentRef,
)
from .vehicle_sharing_place_assignment_ref import (
    VehicleSharingPlaceAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePlaceAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "vehicleServicePlaceAssignmentRefs_RelStructure"

    vehicle_service_place_assignment_ref: Optional[
        Union[
            VehiclePoolingPlaceAssignmentRef,
            VehicleSharingPlaceAssignmentRef,
            TaxiServicePlaceAssignmentRef,
            VehicleServicePlaceAssignmentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingPlaceAssignmentRef",
                    "type": VehiclePoolingPlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingPlaceAssignmentRef",
                    "type": VehicleSharingPlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServicePlaceAssignmentRef",
                    "type": TaxiServicePlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePlaceAssignmentRef",
                    "type": VehicleServicePlaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
