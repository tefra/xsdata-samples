from __future__ import annotations

from dataclasses import dataclass, field

from .fare_product_version_structure import FareProductVersionStructure
from .preassigned_fare_product_enumeration import (
    PreassignedFareProductEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PreassignedFareProductVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "PreassignedFareProduct_VersionStructure"

    product_type: None | PreassignedFareProductEnumeration = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
