from collections.abc import Iterable
from dataclasses import dataclass, field

from .delivery_variant import DeliveryVariant
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeliveryVariantsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deliveryVariants_RelStructure"

    delivery_variant: Iterable[DeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
