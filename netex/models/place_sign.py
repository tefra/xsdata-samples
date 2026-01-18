from __future__ import annotations

from dataclasses import dataclass

from .place_sign_structure import PlaceSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceSign(PlaceSignStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
