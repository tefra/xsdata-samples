from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LocationStructure1:
    class Meta:
        name = "LocationStructure"

    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        }
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        }
    )
    coordinates: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
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
