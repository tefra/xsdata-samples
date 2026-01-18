from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPduSubtypesEnum(Enum):
    CONTAINER_I_PDU = "CONTAINER-I-PDU"
    DCM_I_PDU = "DCM-I-PDU"
    GENERAL_PURPOSE_I_PDU = "GENERAL-PURPOSE-I-PDU"
    I_PDU = "I-PDU"
    I_SIGNAL_I_PDU = "I-SIGNAL-I-PDU"
    J_1939_DCM_I_PDU = "J-1939-DCM-I-PDU"
    MULTIPLEXED_I_PDU = "MULTIPLEXED-I-PDU"
    N_PDU = "N-PDU"
    SECURED_I_PDU = "SECURED-I-PDU"
    USER_DEFINED_I_PDU = "USER-DEFINED-I-PDU"
    XCP_PDU = "XCP-PDU"
