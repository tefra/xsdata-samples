from __future__ import annotations

from dataclasses import dataclass

from .price_group_ref_structure import PriceGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceGroupRef(PriceGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
