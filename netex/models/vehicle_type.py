from __future__ import annotations

from dataclasses import dataclass

from .vehicle_type_version_structure import VehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleType(VehicleTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
