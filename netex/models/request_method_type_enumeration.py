from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RequestMethodTypeEnumeration(Enum):
    NONE_REQUIRED = "noneRequired"
    HAND_SIGNAL = "handSignal"
    TURN_ON_LIGHT = "turnOnLight"
    STOP_BUTTON = "stopButton"
    PHONE_CALL = "phoneCall"
    MOBILE_APP = "mobileApp"
    SMS = "sms"
    OTHER = "other"
