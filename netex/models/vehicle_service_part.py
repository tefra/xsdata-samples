from __future__ import annotations

from dataclasses import dataclass

from .vehicle_service_part_version_structure import (
    VehicleServicePartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServicePart(VehicleServicePartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
