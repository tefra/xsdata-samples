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

    class_in_frame_ref_or_class_in_frame: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ClassInFrameRef",
                    "type": ClassInFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassInFrame",
                    "type": ClassInFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
