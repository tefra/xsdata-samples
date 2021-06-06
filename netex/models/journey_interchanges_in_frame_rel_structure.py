from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_journey_interchange import ServiceJourneyInterchange
from .service_journey_pattern_interchange import ServiceJourneyPatternInterchange

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyInterchangesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyInterchangesInFrame_RelStructure"

    service_journey_pattern_interchange: List[ServiceJourneyPatternInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_interchange: List[ServiceJourneyInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
