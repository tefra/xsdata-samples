from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_service_version_structure import (
    VehiclePoolingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChauffeuredVehicleServiceVersionStructure(
    VehiclePoolingServiceVersionStructure
):
    class Meta:
        name = "ChauffeuredVehicleService_VersionStructure"
