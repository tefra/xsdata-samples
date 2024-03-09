from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "seriesConstraintRefs_RelStructure"

    series_constraint_ref: List[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
