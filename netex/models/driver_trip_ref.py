from __future__ import annotations

from dataclasses import dataclass

from .driver_trip_ref_structure import DriverTripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverTripRef(DriverTripRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
