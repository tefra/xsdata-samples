from dataclasses import dataclass, field
from typing import List
from .class_in_frame import ClassInFrame
from .class_in_frame_ref import ClassInFrameRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassesInRepositoryRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "classesInRepository_RelStructure"

    class_in_frame_ref: List[ClassInFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassInFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_in_frame: List[ClassInFrame] = field(
        default_factory=list,
        metadata={
            "name": "ClassInFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
