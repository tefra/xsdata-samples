from __future__ import annotations

from dataclasses import dataclass

from .parking_price_ref_structure import ParkingPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPriceRef(ParkingPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
