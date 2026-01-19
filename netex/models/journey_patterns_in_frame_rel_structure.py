from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .dead_run_journey_pattern import DeadRunJourneyPattern
from .sections_in_sequence_rel_structure import JourneyPattern
from .service_journey_pattern import ServiceJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPatternsInFrame_RelStructure"

    journey_pattern: Sequence[
        ServiceJourneyPattern | DeadRunJourneyPattern | JourneyPattern
    ] = field(
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
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
