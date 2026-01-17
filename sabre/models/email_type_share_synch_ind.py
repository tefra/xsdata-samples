from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class EmailTypeShareSynchInd(Enum):
    """
    value="Inherit" Permission for sharing data for synchronization of
    information held by other travel service providers.
    """

    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"
