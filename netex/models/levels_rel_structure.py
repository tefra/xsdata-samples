from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.level import Level
from netex.models.level_ref import LevelRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LevelsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "levels_RelStructure"

    level_ref: List[LevelRef] = field(
        default_factory=list,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    level: List[Level] = field(
        default_factory=list,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
