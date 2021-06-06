from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .quay import Quay
from .quay_ref import QuayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QuaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "quays_RelStructure"

    quay_ref: List[QuayRef] = field(
        default_factory=list,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay: List[Quay] = field(
        default_factory=list,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
