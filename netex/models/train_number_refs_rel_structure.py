from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumberRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "trainNumberRefs_RelStructure"

    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
