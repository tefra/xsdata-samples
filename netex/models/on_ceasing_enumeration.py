from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnCeasingEnumeration(Enum):
    IMMEDIATE_TERMINATION = "immediateTermination"
    USE_UNTIL_EXPIRY = "useUntilExpiry"
    TERMINATE_AFTER_GRACE_PERIOD = "terminateAfterGracePeriod"
    AUTOMATICALLY_SUBSTITUTE_PRODUCT = "automaticallySubstituteProduct"
    NO_ACTION = "noAction"
    OTHER = "other"
