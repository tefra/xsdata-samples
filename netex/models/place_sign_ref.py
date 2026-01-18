from __future__ import annotations

from dataclasses import dataclass

from .place_sign_ref_structure import PlaceSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceSignRef(PlaceSignRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
