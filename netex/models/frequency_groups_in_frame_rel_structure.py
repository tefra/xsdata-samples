from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .headway_journey_group import HeadwayJourneyGroup
from .rhythmical_journey_group import RhythmicalJourneyGroup

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyGroupsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "frequencyGroupsInFrame_RelStructure"

    headway_journey_group_or_rhythmical_journey_group: Iterable[
        Union[HeadwayJourneyGroup, RhythmicalJourneyGroup]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
