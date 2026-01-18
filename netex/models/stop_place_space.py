from __future__ import annotations

from dataclasses import dataclass

from .stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceSpace(StopPlaceSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
