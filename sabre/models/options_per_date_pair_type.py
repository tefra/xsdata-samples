from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class OptionsPerDatePairType:
    """
    Attributes:
        departure: Departure date
        return_value: Return date
        min: Minimum number of options per date/date pair
        max: Maximum number of options per date/date pair
    """

    departure: None | str = field(
        default=None,
        metadata={
            "name": "Departure",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
        },
    )
    return_value: None | str = field(
        default=None,
        metadata={
            "name": "Return",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
        },
    )
    min: None | int = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Attribute",
            "required": True,
        },
    )
    max: None | int = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Attribute",
            "required": True,
        },
    )
