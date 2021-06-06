from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .headway_journey_group import HeadwayJourneyGroup
from .rhythmical_journey_group import RhythmicalJourneyGroup

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyGroupsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "frequencyGroupsInFrame_RelStructure"

    headway_journey_group: List[HeadwayJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rhythmical_journey_group: List[RhythmicalJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "RhythmicalJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
