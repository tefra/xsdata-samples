from __future__ import annotations

from dataclasses import dataclass

from .fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementPriceRefStructure(FarePriceRefStructure):
    pass
