from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .destination_display_variant import DestinationDisplayVariant
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "destinationDisplayVariants_RelStructure"

    destination_display_variant: Sequence[DestinationDisplayVariant] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
