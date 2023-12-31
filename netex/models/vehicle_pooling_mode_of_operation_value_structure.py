from dataclasses import dataclass, field
from typing import Optional
from .alternative_mode_of_operation_value_structure import (
    AlternativeModeOfOperationValueStructure,
)
from .vehicle_pooling_type_enumeration import VehiclePoolingTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingModeOfOperationValueStructure(
    AlternativeModeOfOperationValueStructure
):
    class Meta:
        name = "VehiclePoolingModeOfOperation_ValueStructure"

    vehicle_pooling_type: Optional[VehiclePoolingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VehiclePoolingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
