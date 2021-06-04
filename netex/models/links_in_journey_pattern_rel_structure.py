from dataclasses import dataclass, field
from typing import List
from netex.models.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.models.timing_link_in_journey_pattern import TimingLinkInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinksInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "linksInJourneyPattern_RelStructure"

    service_link_in_journey_pattern: List[ServiceLinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_in_journey_pattern: List[TimingLinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
