from dataclasses import dataclass

from .class_relationship_in_frame_structure import (
    ClassRelationshipInFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassRelationshipInFrame(ClassRelationshipInFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
