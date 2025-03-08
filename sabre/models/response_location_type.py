from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ResponseLocationType:
    """
    Code and optional string to describe a location point.

    Attributes:
        value:
        location_code: Location identifying code.
        code_context: Identifies the context of the identifying code,
            such as IATA, ARC, or internal code, etc.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    location_code: None | str = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    code_context: str = field(
        default="IATA",
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
