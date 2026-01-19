from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .call import Call
from .dated_call import DatedCall
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "calls_RelStructure"

    call: Sequence[DatedCall | Call] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedCall",
                    "type": DatedCall,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Call",
                    "type": Call,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
