from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .call import Call
from .dated_call import DatedCall
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "calls_RelStructure"

    call: Iterable[DatedCall | Call] = field(
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
