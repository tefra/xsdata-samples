from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DistributionChannelTypeEnumeration(Enum):
    AT_STOP = "atStop"
    ON_BOARD = "onBoard"
    ONLINE = "online"
    ONLINE_ACCOUNT = "onlineAccount"
    TELEPHONE = "telephone"
    ELECTRONIC_PASS = "electronicPass"
    POSTAL = "postal"
    MOBILE_DEVICE = "mobileDevice"
    AGENCY = "agency"
    TOUR_OPERATOR = "tourOperator"
    OTHER = "other"
