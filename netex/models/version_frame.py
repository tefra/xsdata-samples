from dataclasses import dataclass
from netex.models.version_frame_version_structure import VersionFrameVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrame(VersionFrameVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
