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

    class_in_frame_ref_or_class_ref: List[object] = field(
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
                    "name": "ClassRef",
                    "type": ClassRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
