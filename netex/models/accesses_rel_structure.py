from dataclasses import dataclass, field
from typing import List
from .access import Access
from .access_ref import AccessRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accesses_RelStructure"

    access_ref: List[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access: List[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
