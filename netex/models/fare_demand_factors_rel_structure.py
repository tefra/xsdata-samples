from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .fare_demand_factor import FareDemandFactor
from .fare_demand_factor_ref import FareDemandFactorRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareDemandFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareDemandFactors_RelStructure"

    fare_demand_factor_ref_or_fare_demand_factor: Iterable[
        FareDemandFactorRef | FareDemandFactor
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
