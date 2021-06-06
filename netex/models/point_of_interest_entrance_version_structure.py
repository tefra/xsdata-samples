from dataclasses import dataclass
from .site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "PointOfInterestEntrance_VersionStructure"
