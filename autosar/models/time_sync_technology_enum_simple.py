from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TimeSyncTechnologyEnumSimple(Enum):
    """
    :cvar AVB_IEEE_802_1_AS: Ethernet AVB compliant IEEE802.1AS
        Precision Time Protocol
    :cvar NTP_RFC_958: Network Time Protocol (NTP)
    :cvar PTP_IEEE_1588_2002: Precision Time Protocol (PTP) IEEE
        1588-2002
    :cvar PTP_IEEE_1588_2008: Precision Time Protocol (PTP) IEEE
        1588-2008
    """

    AVB_IEEE_802_1_AS = "AVB--IEEE-802--1-AS"
    NTP_RFC_958 = "NTP--RFC-958"
    PTP_IEEE_1588_2002 = "PTP--IEEE-1588--2002"
    PTP_IEEE_1588_2008 = "PTP--IEEE-1588--2008"
