from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .fare_quota_factor import FareQuotaFactor
from .fare_quota_factor_ref import FareQuotaFactorRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareQuotaFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareQuotaFactors_RelStructure"

    fare_quota_factor_ref_or_fare_quota_factor: Sequence[
        FareQuotaFactorRef | FareQuotaFactor
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
