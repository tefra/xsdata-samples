from __future__ import annotations

from dataclasses import dataclass

from .taxi_parking_area_version_structure import (
    TaxiParkingAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiParkingArea(TaxiParkingAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
