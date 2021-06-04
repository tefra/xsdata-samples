from dataclasses import dataclass
from netex.models.infrastructure_frame_ref_structure import InfrastructureFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureFrameRef(InfrastructureFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
