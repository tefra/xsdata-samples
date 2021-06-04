from dataclasses import dataclass
from netex.models.class_attribute_in_frame_structure import ClassAttributeInFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassAttributeInFrame(ClassAttributeInFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
