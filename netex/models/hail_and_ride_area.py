from __future__ import annotations

from dataclasses import dataclass

from .hail_and_ride_area_version_structure import (
    HailAndRideAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HailAndRideArea(HailAndRideAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
