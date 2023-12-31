from dataclasses import dataclass
from .vehicle_sharing_mode_of_operation_ref_structure import (
    VehicleSharingModeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingRef(VehicleSharingModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
