from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .controllable_element import ControllableElement
from .controllable_element_ref import ControllableElementRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "controllableElements_RelStructure"

    controllable_element_ref_or_controllable_element: Iterable[
        ControllableElementRef | ControllableElement
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElement",
                    "type": ControllableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
