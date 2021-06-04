from dataclasses import dataclass, field
from typing import List
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.line_ref import LineRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "lineRefs_RelStructure"

    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    line_ref: List[LineRef] = field(
        default_factory=list,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
