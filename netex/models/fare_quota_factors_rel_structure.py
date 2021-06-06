from dataclasses import dataclass, field
from typing import List
from .fare_quota_factor import FareQuotaFactor
from .fare_quota_factor_ref import FareQuotaFactorRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareQuotaFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareQuotaFactors_RelStructure"

    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_quota_factor: List[FareQuotaFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
