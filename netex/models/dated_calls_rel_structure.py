from collections.abc import Iterable
from dataclasses import dataclass, field

from .dated_call import DatedCall
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedCallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "datedCalls_RelStructure"

    dated_call: Iterable[DatedCall] = field(
        default_factory=list,
        metadata={
            "name": "DatedCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        },
    )
