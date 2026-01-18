from __future__ import annotations

from dataclasses import dataclass

from .place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Place(PlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
