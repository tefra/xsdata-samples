from dataclasses import dataclass

from .composite_frame_ref_structure import CompositeFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompositeFrameRef(CompositeFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
