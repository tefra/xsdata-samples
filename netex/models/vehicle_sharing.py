from dataclasses import dataclass

from .vehicle_sharing_mode_of_operation_value_structure import (
    VehicleSharingModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharing(VehicleSharingModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
