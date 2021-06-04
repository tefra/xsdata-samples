from dataclasses import dataclass, field
from typing import List
from netex.models.fare_demand_factor import FareDemandFactor
from netex.models.fare_demand_factor_ref import FareDemandFactorRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareDemandFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareDemandFactors_RelStructure"

    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_demand_factor: List[FareDemandFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
