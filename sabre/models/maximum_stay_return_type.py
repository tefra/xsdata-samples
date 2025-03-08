from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class MaximumStayReturnType(Enum):
    """
    Attributes:
        C: Return travel must be Completed.
        S: Return travel must be Started.
    """

    C = "C"
    S = "S"
