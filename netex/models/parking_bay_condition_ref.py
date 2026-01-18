from __future__ import annotations

from dataclasses import dataclass

from .parking_bay_status_ref_structure import ParkingBayStatusRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayConditionRef(ParkingBayStatusRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
