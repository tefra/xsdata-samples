from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_accounting import JourneyAccounting
from .journey_accounting_ref import JourneyAccountingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyAccountingsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyAccountings_RelStructure"

    journey_accounting_ref_or_journey_accounting: Sequence[
        JourneyAccountingRef | JourneyAccounting
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyAccountingRef",
                    "type": JourneyAccountingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyAccounting",
                    "type": JourneyAccounting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
