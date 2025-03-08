from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class PassengerStatusType(Enum):
    """
    Attributes:
        R: Residency.
        E: Employment.
        N: Nationality.
    """

    R = "R"
    E = "E"
    N = "N"
