from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionRenewalPolicyEnumeration(Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    AUTOMATIC_ON_CONFIRMATION = "automaticOnConfirmation"
    NONE_VALUE = "none"
    OTHER = "other"
