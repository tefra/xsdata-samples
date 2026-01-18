from __future__ import annotations

from dataclasses import dataclass

from .driver_trip_time_version_structure import DriverTripTimeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverTripTime(DriverTripTimeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
