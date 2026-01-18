from __future__ import annotations

from dataclasses import dataclass, field

from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "GeographicalIntervalPrice_VersionedChildStructure"

    geographical_interval_ref: GeographicalIntervalRef | None = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
