from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .headway_journey_group import HeadwayJourneyGroup
from .headway_journey_group_ref import HeadwayJourneyGroupRef
from .rhythmical_journey_group import RhythmicalJourneyGroup
from .rhythmical_journey_group_ref import RhythmicalJourneyGroupRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyGroupsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "frequencyGroups_RelStructure"

    headway_journey_group_ref: List[HeadwayJourneyGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway_journey_group: List[HeadwayJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rhythmical_journey_group_ref: List[RhythmicalJourneyGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "RhythmicalJourneyGroupRef",
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
