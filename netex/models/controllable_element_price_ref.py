from __future__ import annotations

from dataclasses import dataclass

from .controllable_element_price_ref_structure import (
    ControllableElementPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementPriceRef(ControllableElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
