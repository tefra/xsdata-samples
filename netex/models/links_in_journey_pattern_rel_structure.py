from dataclasses import dataclass, field
from typing import List, Union
from .service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .timing_link_in_journey_pattern import TimingLinkInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinksInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "linksInJourneyPattern_RelStructure"

    service_link_in_journey_pattern_or_timing_link_in_journey_pattern: List[Union[ServiceLinkInJourneyPattern, TimingLinkInJourneyPattern]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceLinkInJourneyPattern",
                    "type": ServiceLinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkInJourneyPattern",
                    "type": TimingLinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
