from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingPaymentProcessEnumeration(Enum):
    FREE = "free"
    PAY_AT_BAY = "payAtBay"
    PAY_AND_DISPLAY = "payAndDisplay"
    PAY_AT_EXIT_BOOTH_MANUAL_COLLECTION = "payAtExitBoothManualCollection"
    PAY_AT_MACHINE_ON_FOOT_PRIOR_TO_EXIT = "payAtMachineOnFootPriorToExit"
    PAY_BY_PREPAID_TOKEN = "payByPrepaidToken"
    PAY_BY_MOBILE_DEVICE = "payByMobileDevice"
    UNDEFINED = "undefined"
    OTHER = "other"
