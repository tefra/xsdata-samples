from __future__ import annotations

from dataclasses import dataclass

from .chauffeured_vehicle_service_ref_structure import (
    ChauffeuredVehicleServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChauffeuredVehicleServiceRef(ChauffeuredVehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
