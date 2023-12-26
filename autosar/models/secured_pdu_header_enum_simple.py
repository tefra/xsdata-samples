from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SecuredPduHeaderEnumSimple(Enum):
    """
    :cvar NO_HEADER: No header included in the SecuredPdu.
    :cvar SECURED_PDU_HEADER_08_BIT: 8 Bit Secured I-PDU Header included
        in the Secured I-PDU.
    :cvar SECURED_PDU_HEADER_16_BIT: 16 Bit Secured I-PDU Header
        included in the Secured I-PDU.
    :cvar SECURED_PDU_HEADER_32_BIT: 32 Bit Secured I-PDU Header
        included in the Secured I-PDU.
    """

    NO_HEADER = "NO-HEADER"
    SECURED_PDU_HEADER_08_BIT = "SECURED-PDU-HEADER-08-BIT"
    SECURED_PDU_HEADER_16_BIT = "SECURED-PDU-HEADER-16-BIT"
    SECURED_PDU_HEADER_32_BIT = "SECURED-PDU-HEADER-32-BIT"
