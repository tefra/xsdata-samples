from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetMacLayerTypeEnumSimple(Enum):
    """
    :cvar X_MII: Mac layer interface (data) bandwith class 100Mbit/s and
        10Mbit/s (e.g. RMII, RvMII, SMII, RvMII)
    :cvar XG_MII: Mac layer interface (data) bandwith class 1Gbit/s
        (e.g. GMII, RGMII, SGMII, RvGMII, USGMII)
    :cvar XXG_MII: Mac layer interface (data) bandwith class 10Gbit/s
    """
    X_MII = "X-MII"
    XG_MII = "XG-MII"
    XXG_MII = "XXG-MII"
