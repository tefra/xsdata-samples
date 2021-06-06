from dataclasses import dataclass
from .infrastructure_version_frame_structure import InfrastructureVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureFrame(InfrastructureVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
