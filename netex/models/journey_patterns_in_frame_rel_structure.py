from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.dead_run_journey_pattern import DeadRunJourneyPattern
from netex.models.journey_pattern_2 import JourneyPattern2
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.link_sequence_version_structure import JourneyPattern1
from netex.models.service_journey_pattern import ServiceJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPatternsInFrame_RelStructure"

    service_journey_pattern: List[ServiceJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern: List[DeadRunJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern: List[JourneyPattern1] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_journey_pattern: List[JourneyPattern2] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_view: List[JourneyPatternView] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
