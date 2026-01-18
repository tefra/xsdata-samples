from __future__ import annotations

from dataclasses import dataclass

from .beacon_point_version_structure import BeaconPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BeaconPoint(BeaconPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
