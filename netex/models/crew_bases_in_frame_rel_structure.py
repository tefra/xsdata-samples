from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .crew_base import CrewBase

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CrewBasesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "crewBasesInFrame_RelStructure"

    crew_base: List[CrewBase] = field(
        default_factory=list,
        metadata={
            "name": "CrewBase",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
