from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.models.geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "GeographicalIntervalPrice_VersionedChildStructure"

    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
