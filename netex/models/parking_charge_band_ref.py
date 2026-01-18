from __future__ import annotations

from dataclasses import dataclass

from .parking_charge_band_ref_structure import ParkingChargeBandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingChargeBandRef(ParkingChargeBandRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
