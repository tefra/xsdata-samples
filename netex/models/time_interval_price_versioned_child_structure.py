from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.models.time_interval_ref import TimeIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "TimeIntervalPrice_VersionedChildStructure"

    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
