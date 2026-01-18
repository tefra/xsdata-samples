from __future__ import annotations

from dataclasses import dataclass

from .geographical_unit_prices_rel_structure import (
    GeographicalUnitPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitPrice(GeographicalUnitPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
