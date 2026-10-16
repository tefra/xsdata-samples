from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnCeasingEnumeration(StrEnum):
    IMMEDIATE_TERMINATION = "immediateTermination"
    USE_UNTIL_EXPIRY = "useUntilExpiry"
    TERMINATE_AFTER_GRACE_PERIOD = "terminateAfterGracePeriod"
    AUTOMATICALLY_SUBSTITUTE_PRODUCT = "automaticallySubstituteProduct"
    NO_ACTION = "noAction"
    OTHER = "other"
