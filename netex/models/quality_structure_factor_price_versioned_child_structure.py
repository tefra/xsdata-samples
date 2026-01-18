from __future__ import annotations

from dataclasses import dataclass, field

from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .fare_quota_factor_ref import FareQuotaFactorRef
from .quality_structure_factor_ref import QualityStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QualityStructureFactorPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "QualityStructureFactorPrice_VersionedChildStructure"

    quality_structure_factor_ref: (
        FareQuotaFactorRef
        | FareDemandFactorRef
        | QualityStructureFactorRef
        | None
    ) = field(
        default=None,
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
            ),
        },
    )
