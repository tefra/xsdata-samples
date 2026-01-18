from collections.abc import Iterable
from dataclasses import dataclass, field

from .fare_quota_factor import FareQuotaFactor
from .fare_quota_factor_ref import FareQuotaFactorRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareQuotaFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareQuotaFactors_RelStructure"

    fare_quota_factor_ref_or_fare_quota_factor: Iterable[
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
