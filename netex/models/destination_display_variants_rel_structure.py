from collections.abc import Iterable
from dataclasses import dataclass, field

from .destination_display_variant import DestinationDisplayVariant
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayVariantsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "destinationDisplayVariants_RelStructure"

    destination_display_variant: Iterable[DestinationDisplayVariant] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
