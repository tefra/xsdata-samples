from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LocationStructure1:
    class Meta:
        name = "LocationStructure"

    longitude_or_latitude_or_coordinates: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Longitude",
                    "type": Decimal,
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_inclusive": Decimal("-180"),
                    "max_inclusive": Decimal("180"),
                },
                {
                    "name": "Latitude",
                    "type": Decimal,
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_inclusive": Decimal("-90"),
                    "max_inclusive": Decimal("90"),
                },
                {
                    "name": "Coordinates",
                    "type": List[str],
                    "namespace": "http://www.siri.org.uk/siri",
                    "default_factory": list,
                    "tokens": True,
                },
            ),
            "max_occurs": 2,
        }
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
