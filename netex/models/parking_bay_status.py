from __future__ import annotations

from dataclasses import dataclass

from .parking_bay_status_value_structure import ParkingBayStatusValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayStatus(ParkingBayStatusValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
