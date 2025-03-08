from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class FlightTypeType(Enum):
    """Identifies a particular type of flight - Direct, Stopover etc.

    Attributes:
        NONSTOP: Flight without plane change and without intermediate
            landing.
        DIRECT: Flight without plane change and possible intermediate
            landing.
        CONNECTION: Flight with plane changes, allowing maximum of 24
            hours for each change
    """

    NONSTOP = "Nonstop"
    DIRECT = "Direct"
    CONNECTION = "Connection"
