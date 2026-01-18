from __future__ import annotations

from dataclasses import dataclass

from .stop_place_version_structure import StopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlace(StopPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
