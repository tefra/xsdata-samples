from __future__ import annotations

from dataclasses import dataclass

from .site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "PointOfInterestEntrance_VersionStructure"
