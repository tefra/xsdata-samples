from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AudioTriggerMethodEnumeration(Enum):
    PRESENCE_DETECTOR = "presenceDetector"
    MOBILE_APP = "mobileApp"
    INTERNET_PAGE = "internetPage"
    SPECIFIC_DEVICE = "specificDevice"
    PUSH_BUTTON = "pushButton"
    OTHER = "other"
