from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class SubscriptionStateEnum(StrEnum):
    """
    The state of a client's current subscription.

    :cvar ACTIVE: The client's subscription as registered with a
        supplier is currently active.
    :cvar SUSPENDED: The client's subscription as registered with a
        supplier is currently suspended.
    """

    ACTIVE = "active"
    SUSPENDED = "suspended"
