from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.stop_area_ref_structure import StopAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAreaRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "stopAreaRefs_RelStructure"

    stop_area_ref: List[StopAreaRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
