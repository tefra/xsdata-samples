from dataclasses import dataclass
from netex.models.common_version_frame_structure import CommonVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonFrame(CommonVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
