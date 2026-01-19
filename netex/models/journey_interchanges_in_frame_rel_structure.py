from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_journey_interchange import ServiceJourneyInterchange
from .service_journey_pattern_interchange import (
    ServiceJourneyPatternInterchange,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyInterchangesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyInterchangesInFrame_RelStructure"

    service_journey_pattern_interchange_or_service_journey_interchange: Sequence[
        ServiceJourneyPatternInterchange | ServiceJourneyInterchange
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternInterchange",
                    "type": ServiceJourneyPatternInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
