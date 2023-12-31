from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PlugTypeEnumeration(Enum):
    UNDEFINED = "undefined"
    TYPE1 = "type1"
    TYPE2 = "type2"
    TYPE3 = "type3"
    TYPE_E = "typeE"
    TYPE_F = "typeF"
    TYPE_G = "typeG"
    TYPE_J = "typeJ"
    COMBINED_CHARGING_SYSTEM = "combinedChargingSystem"
    CCS_COMBO1_PLUG = "ccsCombo1Plug"
    CCS_COMBO2_PLUG = "ccsCombo2Plug"
    TESLA = "tesla"
    NEMA5_20 = "nema5-20"
    AVCON = "avcon"
    CHADE_MO = "CHAdeMO"
    SHOCKPROOF = "shockproof"
