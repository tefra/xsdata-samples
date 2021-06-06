from dataclasses import dataclass
from .site_frame_ref_structure import SiteFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteFrameRef(SiteFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
