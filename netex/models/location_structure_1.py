from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, Optional, Union

from .coordinates_structure import CoordinatesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LocationStructure1:
    class Meta:
        name = "LocationStructure"

    longitude_or_latitude_or_coordinates: Iterable[
        Union[
            "LocationStructure1.Longitude",
            "LocationStructure1.Latitude",
            CoordinatesStructure,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Longitude",
                    "type": ForwardRef("LocationStructure1.Longitude"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Latitude",
                    "type": ForwardRef("LocationStructure1.Latitude"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Coordinates",
                    "type": CoordinatesStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 2,
        },
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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

    @dataclass
    class Longitude:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
                "min_inclusive": Decimal("-180"),
                "max_inclusive": Decimal("180"),
            },
        )

    @dataclass
    class Latitude:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
                "min_inclusive": Decimal("-90"),
                "max_inclusive": Decimal("90"),
            },
        )
