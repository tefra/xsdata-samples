from __future__ import annotations

from dataclasses import dataclass

from .vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRef(VehicleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
