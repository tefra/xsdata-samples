from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ReservationType:
    """
    Attributes:
        status: Reservation status
        real_status: Real reservation status
    """

    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "pattern": r"[A-Z]{1,2}",
        },
    )
    real_status: None | str = field(
        default=None,
        metadata={
            "name": "RealStatus",
            "type": "Attribute",
            "pattern": r"[A-Z]{1,2}",
        },
    )
