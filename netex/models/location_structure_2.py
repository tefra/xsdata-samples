from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .pos import Pos

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocationStructure2:
    class Meta:
        name = "LocationStructure"

    longitude: None | Decimal = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
    latitude: None | Decimal = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    altitude: None | Decimal = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        },
    )
    pos: None | Pos = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    precision: None | Decimal = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    srs_name: None | str = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
