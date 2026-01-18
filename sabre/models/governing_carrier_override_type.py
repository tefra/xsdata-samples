from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class GoverningCarrierOverrideType:
    """
    Attributes:
        airline_code: Airline Carrier Code - override the GOVERNING
            CARRIER to get the fare filed by that carrier.
    """

    airline_code: str = field(
        metadata={
            "name": "AirlineCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
