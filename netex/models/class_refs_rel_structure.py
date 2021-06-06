from dataclasses import dataclass, field
from typing import List
from .class_in_frame_ref import ClassInFrameRef
from .class_ref import ClassRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "classRefs_RelStructure"

    class_in_frame_ref: List[ClassInFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassInFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    class_ref: List[ClassRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
