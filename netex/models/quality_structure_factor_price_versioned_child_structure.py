from dataclasses import dataclass, field
from typing import List, Optional
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .fare_quota_factor_ref import FareQuotaFactorRef
from .quality_structure_factor_ref import QualityStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "QualityStructureFactorPrice_VersionedChildStructure"

    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    quality_structure_factor_ref: Optional[QualityStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "QualityStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
