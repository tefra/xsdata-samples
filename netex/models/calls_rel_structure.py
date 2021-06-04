from dataclasses import dataclass, field
from typing import List
from netex.models.call_1 import Call1
from netex.models.call_2 import Call2
from netex.models.call_z import CallZ
from netex.models.dated_call import DatedCall
from netex.models.dated_call_z import DatedCallZ
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

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
            "min_occurs": 2,
        }
    )
    dated_call: List[DatedCall] = field(
        default_factory=list,
        metadata={
            "name": "DatedCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
    call_z: List[CallZ] = field(
        default_factory=list,
        metadata={
            "name": "Call-Z",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
    call: List[Call2] = field(
        default_factory=list,
        metadata={
            "name": "Call",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
    netex_org_uk_netex_call: List[Call1] = field(
        default_factory=list,
        metadata={
            "name": "Call_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
