from __future__ import annotations

from dataclasses import dataclass

from .time_unit_price_versioned_child_structure import (
    TimeUnitPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitPrice(TimeUnitPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
