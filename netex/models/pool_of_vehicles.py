from __future__ import annotations

from dataclasses import dataclass

from .pool_of_vehicles_version_structure import PoolOfVehiclesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PoolOfVehicles(PoolOfVehiclesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
