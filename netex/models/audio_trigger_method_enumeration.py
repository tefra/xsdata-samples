from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AudioTriggerMethodEnumeration(StrEnum):
    PRESENCE_DETECTOR = "presenceDetector"
    MOBILE_APP = "mobileApp"
    INTERNET_PAGE = "internetPage"
    SPECIFIC_DEVICE = "specificDevice"
    PUSH_BUTTON = "pushButton"
    OTHER = "other"
