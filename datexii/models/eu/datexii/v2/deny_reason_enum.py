from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DenyReasonEnum(Enum):
    """
    Reasons for denial of a request.

    :cvar UNKNOWN_REASON: Reason unknown.
    :cvar WRONG_CATALOGUE: Wrong catalogue specified.
    :cvar WRONG_FILTER: Wrong filter specified.
    :cvar WRONG_ORDER: Wrong order specified.
    :cvar WRONG_PARTNER: Wrong partner specified.
    """

    UNKNOWN_REASON = "unknownReason"
    WRONG_CATALOGUE = "wrongCatalogue"
    WRONG_FILTER = "wrongFilter"
    WRONG_ORDER = "wrongOrder"
    WRONG_PARTNER = "wrongPartner"
