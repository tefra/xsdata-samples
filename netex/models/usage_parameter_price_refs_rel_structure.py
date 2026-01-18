from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .usage_parameter_price_ref import UsageParameterPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterPriceRefsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "usageParameterPriceRefs_RelStructure"

    usage_parameter_price_ref: Iterable[UsageParameterPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
