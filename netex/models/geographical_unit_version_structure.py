from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .fare_unit_version_structure import FareUnitVersionStructure
from .geographical_unit_prices_rel_structure import (
    GeographicalUnitPricesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitVersionStructure(FareUnitVersionStructure):
    class Meta:
        name = "GeographicalUnit_VersionStructure"

    distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: None | GeographicalUnitPricesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
