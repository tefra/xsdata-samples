from dataclasses import dataclass, field
from typing import List
from .call_1 import Call1
from .call_2 import Call2
from .call_z import CallZ
from .dated_call import DatedCall
from .dated_call_z import DatedCallZ
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "calls_RelStructure"

    dated_call_z: List[DatedCallZ] = field(
        default_factory=list,
        metadata={
            "name": "DatedCall-Z",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_call: List[DatedCall] = field(
        default_factory=list,
        metadata={
            "name": "DatedCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    call_z: List[CallZ] = field(
        default_factory=list,
        metadata={
            "name": "Call-Z",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    call: List[Call1] = field(
        default_factory=list,
        metadata={
            "name": "Call",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_call: List[Call2] = field(
        default_factory=list,
        metadata={
            "name": "Call_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
