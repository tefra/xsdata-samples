from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .pool_of_vehicles import PoolOfVehicles

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PoolOfVehiclesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "poolOfVehicles_RelStructure"

    pool_of_vehicles: Iterable[PoolOfVehicles] = field(
        default_factory=list,
        metadata={
            "name": "PoolOfVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
