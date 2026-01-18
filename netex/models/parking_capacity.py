from __future__ import annotations

from dataclasses import dataclass

from .parking_capacity_versioned_child_structure import (
    ParkingCapacityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingCapacity(ParkingCapacityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
