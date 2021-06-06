from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_set import ResponsibilitySet
from .responsibility_set_ref import ResponsibilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "responsibilitySets_RelStructure"

    responsibility_set_ref: List[ResponsibilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_set: List[ResponsibilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
