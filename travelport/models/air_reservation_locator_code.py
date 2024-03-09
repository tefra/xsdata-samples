from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirReservationLocatorCode:
    """
    Identifies the AirReservation LocatorCode within the Universal Record.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
