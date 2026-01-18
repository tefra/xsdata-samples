from __future__ import annotations

from dataclasses import dataclass

from .parking_bay_condition_version_structure import (
    ParkingBayConditionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayCondition(ParkingBayConditionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
