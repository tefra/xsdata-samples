from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class RequestLocationType:
    """
    Code and optional string to describe a location point.

    Attributes:
        value:
        location_code: Location identifying code. Required unless
            AirportsGroup or AllAirports is specified. Cannot appear
            with AirportsGroup nor AllAirports.
        airports_group: Name of the airports group
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
            "pattern": r"[A-Z]{1,8}",
        },
    )
    airports_group: None | str = field(
        default=None,
        metadata={
            "name": "AirportsGroup",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9]{1,40}",
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
