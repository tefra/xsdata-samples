from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .pricing_service import PricingService
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingServicesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pricingServices_RelStructure"

    pricing_service: Iterable[PricingService] = field(
        default_factory=list,
        metadata={
            "name": "PricingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
