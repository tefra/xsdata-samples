from dataclasses import dataclass
from .general_frame_ref_structure import GeneralFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralFrameRef(GeneralFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
