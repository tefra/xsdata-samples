from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_accounting import JourneyAccounting
from .journey_accounting_ref import JourneyAccountingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyAccountingsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyAccountings_RelStructure"

    journey_accounting_ref_or_journey_accounting: Iterable[
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
