from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetPhysicalLayerTypeEnumSimple(Enum):
    """
    :cvar VALUE_1000_BASE_T: Ethernet Standard (IEEE 802.3ab) to support
        1Gbit/s over 4 twisted pairs.
    :cvar VALUE_1000_BASE_T1: Ethernet Standard (IEEE 802.3bp) to
        support 1Gbit/s over a single twisted pair cable.
    :cvar VALUE_100_BASE_T1: Ethernet Standard (IEEE 802.3bw) to support
        100Mbit/s over a single twisted pair cable.  100BASE-T1 is the
        IEEE Standardized version of BroadRReach.
    :cvar VALUE_100_BASE_TX: Ethernet Standard (IEEE 802.3u) to support
        100Mbit/s over two twisted pairs.
    :cvar VALUE_10_BASE_T1_S: Physical layer interface 10BASE-T1S
        (10Mbit/s, 2 pairs). Used for automotive.
    :cvar BASE_T: BaseT physical layer (10BaseT, 100BaseT, 1000BaseT)
    :cvar BROAD_R_REACH: BroadR-Reach physical layer
    :cvar IEEE802_11_P: Ethernet Standard (IEEE 802.11p) to support
        wireless communication in vehicular environments.
    :cvar RTPGE: Reduced Twisted Pair Gigabit Ethernet (RTPGE) physical
        layer
    :cvar X_MII: Media Independent Interface (MII) physical layer
    :cvar X_MMI: This enumeration literal is set to obsolete and will be
        removed in future. Please use xMII instead. Old description:
        Media Independent Interface (MII) physical layer
    """

    VALUE_1000_BASE_T = "1000BASE-T"
    VALUE_1000_BASE_T1 = "1000BASE-T1"
    VALUE_100_BASE_T1 = "100BASE-T1"
    VALUE_100_BASE_TX = "100BASE-TX"
    VALUE_10_BASE_T1_S = "10BASE-T1S"
    BASE_T = "BASE-T"
    BROAD_R_REACH = "BROAD-R-REACH"
    IEEE802_11_P = "IEEE802-11P"
    RTPGE = "RTPGE"
    X_MII = "X-MII"
    X_MMI = "X-MMI"
