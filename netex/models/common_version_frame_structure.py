from dataclasses import dataclass
from .version_frame_version_structure import VersionFrameVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonVersionFrameStructure(VersionFrameVersionStructure):
    class Meta:
        name = "Common_VersionFrameStructure"
