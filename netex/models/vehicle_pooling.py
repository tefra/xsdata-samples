from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_mode_of_operation_value_structure import (
    VehiclePoolingModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePooling(VehiclePoolingModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
