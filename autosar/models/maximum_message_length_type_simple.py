from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MaximumMessageLengthTypeSimple(Enum):
    """
    :cvar I_4_G: SF-E allowed (SF of arbitrary length depending on
        FrTpPduLength), up to (2**32)-1 byte message length (all FF-x
        allowed).
    :cvar ISO: Up to (2**12)-1 Byte message length (No FF-Ex or SF-E or
        AF shall be used and recognized).
    :cvar ISO_6: As ISO, but the maximum payload length is limited to 6
        byte (SF-I, FF-I, CF). This is necessary to route TP on CAN when
        using Extended Addressing or Mixed Addressing on CAN.
    """

    I_4_G = "I-4-G"
    ISO = "ISO"
    ISO_6 = "ISO-6"
