from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResellWhenEnumeration(Enum):
    NEVER = "never"
    WITHIN_PURCHASE_GRACE_PERIOD = "withinPurchaseGracePeriod"
    BEFORE_START_OF_VALIDITY = "beforeStartOfValidity"
    AFTER_START_OF_VALIDITY = "afterStartOfValidity"
    AFTER_END_OF_VALIDITY = "afterEndOfValidity"
    BEFORE_FIRST_USE = "beforeFirstUse"
    AFTER_FIRST_USE = "afterFirstUse"
    BEFORE_VALIDATION = "beforeValidation"
    AFTER_VALIDATION = "afterValidation"
    WITHIN_SPECIFIED_WINDOW = "withinSpecifiedWindow"
    ANY_TIME = "anyTime"
    OTHER = "other"
