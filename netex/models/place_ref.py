from __future__ import annotations

from dataclasses import dataclass

from .place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceRef(PlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
