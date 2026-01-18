from __future__ import annotations

from dataclasses import dataclass

from .price_unit_ref_structure import PriceUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnitRef(PriceUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
