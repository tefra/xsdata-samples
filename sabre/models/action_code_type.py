from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class ActionCodeType(StrEnum):
    """
    Identifies the action code for a booking - OK, Waitlist etc.
    """

    OK = "OK"
    WAITLIST = "Waitlist"
    OTHER = "Other"
