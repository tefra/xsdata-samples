from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FlightStopsAsConnectionsType:
    """
    Treat all stops as connections.
    """

    ind: None | bool = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Attribute",
            "required": True,
        },
    )
