from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RequestMethodTypeEnumeration(StrEnum):
    NONE_REQUIRED = "noneRequired"
    HAND_SIGNAL = "handSignal"
    TURN_ON_LIGHT = "turnOnLight"
    STOP_BUTTON = "stopButton"
    PHONE_CALL = "phoneCall"
    MOBILE_APP = "mobileApp"
    SMS = "sms"
    SPEAK_TO_DRIVER_ONBOARD = "speakToDriverOnboard"
    OTHER = "other"
