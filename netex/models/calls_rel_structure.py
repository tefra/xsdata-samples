from dataclasses import dataclass, field
from typing import List, Union
from .call import Call
from .call_z import CallZ
from .dated_call import DatedCall
from .dated_call_z import DatedCallZ
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "calls_RelStructure"

    choice: List[Union[DatedCallZ, DatedCall, CallZ, Call]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedCall-Z",
                    "type": DatedCallZ,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedCall",
                    "type": DatedCall,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Call-Z",
                    "type": CallZ,
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
