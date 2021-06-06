from dataclasses import dataclass, field
from typing import List
from .controllable_element import ControllableElement
from .controllable_element_ref import ControllableElementRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "controllableElements_RelStructure"

    controllable_element_ref: List[ControllableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element: List[ControllableElement] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
