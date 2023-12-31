from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .pool_of_vehicles import PoolOfVehicles

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PoolOfVehiclesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "poolOfVehicles_RelStructure"

    pool_of_vehicles: List[PoolOfVehicles] = field(
        default_factory=list,
        metadata={
            "name": "PoolOfVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
