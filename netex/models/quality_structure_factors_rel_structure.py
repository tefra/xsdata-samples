from dataclasses import dataclass, field
from typing import List
from .fare_demand_factor import FareDemandFactor
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor import FareQuotaFactor
from .fare_quota_factor_ref import FareQuotaFactorRef
from .quality_structure_factor_1 import QualityStructureFactor1
from .quality_structure_factor_2 import QualityStructureFactor2
from .quality_structure_factor_ref import QualityStructureFactorRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "qualityStructureFactors_RelStructure"

    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor_ref: List[QualityStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorRef",
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
    fare_demand_factor: List[FareDemandFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor: List[QualityStructureFactor1] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_quality_structure_factor: List[QualityStructureFactor2] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
