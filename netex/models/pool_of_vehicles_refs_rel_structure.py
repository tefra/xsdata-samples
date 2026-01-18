from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .pool_of_vehicles_ref import PoolOfVehiclesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PoolOfVehiclesRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "PoolOfVehiclesRefs_RelStructure"

    pool_of_vehicles_ref: Iterable[PoolOfVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "PoolOfVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
