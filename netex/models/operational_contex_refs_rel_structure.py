from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .operational_context_ref import OperationalContextRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperationalContexRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "operationalContexRefs_RelStructure"

    operational_context_ref: List[OperationalContextRef] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
