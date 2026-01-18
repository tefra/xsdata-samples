from __future__ import annotations

from dataclasses import dataclass

from .fare_product_version_structure import FareProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProduct1(FareProductVersionStructure):
    class Meta:
        name = "FareProduct"
        namespace = "http://www.netex.org.uk/netex"
