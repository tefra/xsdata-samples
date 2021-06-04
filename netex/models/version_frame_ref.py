from dataclasses import dataclass
from netex.models.version_frame_ref_structure import VersionFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameRef(VersionFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
