from __future__ import annotations

from dataclasses import dataclass

from .validable_element_price_ref_structure import (
    ValidableElementPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementPriceRef(ValidableElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
