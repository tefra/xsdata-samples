from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .level import Level
from .level_ref import LevelRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LevelsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "levels_RelStructure"

    level_ref_or_level: Iterable[LevelRef | Level] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LevelRef",
                    "type": LevelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Level",
                    "type": Level,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
