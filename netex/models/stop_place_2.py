from dataclasses import dataclass

from .site_version_structure import SiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlace2(SiteVersionStructure):
    class Meta:
        name = "StopPlace_"
        namespace = "http://www.netex.org.uk/netex"
