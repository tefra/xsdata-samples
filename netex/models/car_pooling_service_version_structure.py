from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_service_version_structure import (
    VehiclePoolingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarPoolingServiceVersionStructure(VehiclePoolingServiceVersionStructure):
    class Meta:
        name = "CarPoolingService_VersionStructure"
