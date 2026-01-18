from __future__ import annotations

from dataclasses import dataclass, field

from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "FareStructureElementPrice_VersionedChildStructure"

    fare_structure_element_ref: None | FareStructureElementRef = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
