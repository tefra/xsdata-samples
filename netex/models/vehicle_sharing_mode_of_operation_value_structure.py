from dataclasses import dataclass, field

from .alternative_mode_of_operation_value_structure import (
    AlternativeModeOfOperationValueStructure,
)
from .vehicle_sharing_type_enumeration import VehicleSharingTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingModeOfOperationValueStructure(
    AlternativeModeOfOperationValueStructure
):
    class Meta:
        name = "VehicleSharingModeOfOperation_ValueStructure"

    vehicle_sharing_type: VehicleSharingTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "VehicleSharingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
