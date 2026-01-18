from dataclasses import dataclass, field

from .individual_traveller_ref import IndividualTravellerRef
from .trip_leg_ref import TripLegRef
from .trip_ref import TripRef
from .validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)
from .vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchaseParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    class Meta:
        name = "CustomerPurchaseParameterAssignment_VersionStructure"

    individual_traveller_ref: IndividualTravellerRef | None = field(
        default=None,
        metadata={
            "name": "IndividualTravellerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_pooling_driver_info_ref: VehiclePoolingDriverInfoRef | None = (
        field(
            default=None,
            metadata={
                "name": "VehiclePoolingDriverInfoRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    trip_ref: TripRef | None = field(
        default=None,
        metadata={
            "name": "TripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trip_leg_ref: TripLegRef | None = field(
        default=None,
        metadata={
            "name": "TripLegRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
