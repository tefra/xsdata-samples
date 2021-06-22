from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .dead_run_journey_pattern import DeadRunJourneyPattern
from .journey_pattern_2 import JourneyPattern2
from .journey_pattern_view import JourneyPatternView
from .link_sequence_version_structure import JourneyPattern1
from .service_journey_pattern import ServiceJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPatternsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPattern",
                    "type": ServiceJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPattern",
                    "type": DeadRunJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern_",
                    "type": JourneyPattern2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternView",
                    "type": JourneyPatternView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
