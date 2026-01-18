from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_service_ref_structure import (
    VehiclePoolingServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChauffeuredVehicleServiceRefStructure(VehiclePoolingServiceRefStructure):
    pass
