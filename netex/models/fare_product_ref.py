from __future__ import annotations

from dataclasses import dataclass

from .fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductRef(FareProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
