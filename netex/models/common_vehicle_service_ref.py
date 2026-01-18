from __future__ import annotations

from dataclasses import dataclass

from .common_vehicle_service_ref_structure import (
    CommonVehicleServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonVehicleServiceRef(CommonVehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
