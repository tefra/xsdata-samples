from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class MileageDisplayType:
    """
    Attributes:
        type_value: Mileage display type
        city: Mileage display city
        surcharge: Mileage surcharge percentage
    """

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    surcharge: None | int = field(
        default=None,
        metadata={
            "name": "Surcharge",
            "type": "Attribute",
        },
    )
