from __future__ import annotations

from dataclasses import dataclass

from .vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeRef(VehicleTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
