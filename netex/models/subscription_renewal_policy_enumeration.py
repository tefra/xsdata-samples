from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionRenewalPolicyEnumeration(StrEnum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    AUTOMATIC_ON_CONFIRMATION = "automaticOnConfirmation"
    NONE = "none"
    OTHER = "other"
