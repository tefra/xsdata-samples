from dataclasses import dataclass, field
from typing import List, Union

from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "lineRefs_RelStructure"

    line_ref: List[Union[FlexibleLineRef, LineRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
