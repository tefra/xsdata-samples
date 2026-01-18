from __future__ import annotations

from dataclasses import dataclass

from .chauffeured_vehicle_service_version_structure import (
    ChauffeuredVehicleServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChauffeuredVehicleService(ChauffeuredVehicleServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
