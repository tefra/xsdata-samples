from __future__ import annotations

from dataclasses import dataclass

from .vehicle_service_ref_structure import VehicleServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServiceRef(VehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
