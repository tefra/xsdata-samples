from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .pos import Pos

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LocationStructure2:
    class Meta:
        name = "LocationStructure"

    longitude: Decimal | None = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
    latitude: Decimal | None = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    altitude: Decimal | None = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        },
    )
    pos: Pos | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    precision: Decimal | None = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    srs_name: str | None = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
