from dataclasses import dataclass, field
from typing import Optional
from .alternative_mode_of_operation_value_structure import (
    AlternativeModeOfOperationValueStructure,
)
from .vehicle_rental_type_enumeration import VehicleRentalTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleRentalModeOfOperationValueStructure(
    AlternativeModeOfOperationValueStructure
):
    class Meta:
        name = "VehicleRentalModeOfOperation_ValueStructure"

    vehicle_rental_type: Optional[VehicleRentalTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleRentalType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
