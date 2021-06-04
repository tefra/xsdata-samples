from dataclasses import dataclass, field
from typing import List
from netex.models.authority import Authority
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.operator import Operator

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transportOperatorsInFrame_RelStructure"

    authority: List[Authority] = field(
        default_factory=list,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator: List[Operator] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
