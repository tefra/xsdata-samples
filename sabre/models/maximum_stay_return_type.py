from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class MaximumStayReturnType(StrEnum):
    """
    Attributes:
        C: Return travel must be Completed.
        S: Return travel must be Started.
    """

    C = "C"
    S = "S"
