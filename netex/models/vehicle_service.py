from __future__ import annotations

from dataclasses import dataclass

from .vehicle_service_version_structure import VehicleServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleService(VehicleServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
