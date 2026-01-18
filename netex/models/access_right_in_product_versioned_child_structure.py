from __future__ import annotations

from dataclasses import dataclass, field

from .fare_element_in_sequence_versioned_child_structure import (
    FareElementInSequenceVersionedChildStructure,
)
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .supplement_product_ref import SupplementProductRef
from .validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightInProductVersionedChildStructure(
    FareElementInSequenceVersionedChildStructure
):
    class Meta:
        name = "AccessRightInProduct_VersionedChildStructure"

    validable_element_ref: ValidableElementRef | None = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preassigned_fare_product_ref: (
        SupplementProductRef | PreassignedFareProductRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
