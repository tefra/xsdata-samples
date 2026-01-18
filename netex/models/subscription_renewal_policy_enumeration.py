from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionRenewalPolicyEnumeration(Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    AUTOMATIC_ON_CONFIRMATION = "automaticOnConfirmation"
    NONE = "none"
    OTHER = "other"
