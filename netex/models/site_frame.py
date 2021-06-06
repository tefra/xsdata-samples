from dataclasses import dataclass
from .site_version_frame_structure import SiteVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteFrame(SiteVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
