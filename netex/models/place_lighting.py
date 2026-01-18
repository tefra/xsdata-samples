from __future__ import annotations

from dataclasses import dataclass

from .place_lighting_version_structure import PlaceLightingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceLighting(PlaceLightingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
