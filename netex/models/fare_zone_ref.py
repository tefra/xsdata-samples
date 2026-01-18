from __future__ import annotations

from dataclasses import dataclass

from .fare_zone_ref_structure import FareZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZoneRef(FareZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
