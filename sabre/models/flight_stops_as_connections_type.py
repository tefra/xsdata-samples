from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FlightStopsAsConnectionsType:
    """
    Treat all stops as connections.
    """

    ind: bool = field(
        metadata={
            "name": "Ind",
            "type": "Attribute",
            "required": True,
        }
    )
