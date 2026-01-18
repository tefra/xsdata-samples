from __future__ import annotations

from dataclasses import dataclass

from .road_address_ref_structure import RoadAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadAddressRef(RoadAddressRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
