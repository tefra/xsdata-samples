from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_pattern_view import JourneyPatternView
from .service_pattern import ServicePattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicePatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "servicePatternsInFrame_RelStructure"

    service_pattern: List[ServicePattern] = field(
        default_factory=list,
        metadata={
            "name": "ServicePattern",
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