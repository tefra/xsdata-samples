from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .pos import Pos

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LocationStructure2:
    class Meta:
        name = "LocationStructure"

    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    altitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        },
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    precision: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
