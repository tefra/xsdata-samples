from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .fare_demand_factor import FareDemandFactor
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor import FareQuotaFactor
from .fare_quota_factor_ref import FareQuotaFactorRef
from .quality_structure_factor import QualityStructureFactor
from .quality_structure_factor_ref import QualityStructureFactorRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "qualityStructureFactors_RelStructure"

    quality_structure_factor_ref_or_quality_structure_factor: Iterable[
        Union[
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            FareQuotaFactor,
            FareDemandFactor,
            QualityStructureFactor,
        ]
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
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactor",
                    "type": QualityStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
