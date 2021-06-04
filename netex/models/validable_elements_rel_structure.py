from dataclasses import dataclass, field
from typing import List
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "validableElements_RelStructure"

    validable_element_ref: List[ValidableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element: List[ValidableElement] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
