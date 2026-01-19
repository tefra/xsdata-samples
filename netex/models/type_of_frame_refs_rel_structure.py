from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_frame_ref import TypeOfFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFrameRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFrameRefs_RelStructure"

    type_of_frame_ref: Sequence[TypeOfFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
