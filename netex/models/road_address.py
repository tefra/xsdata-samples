from __future__ import annotations

from dataclasses import dataclass

from .road_address_version_structure import RoadAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadAddress(RoadAddressVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
