from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoAdConnectorTypeSimple(Enum):
    """
    :cvar DO_IP: Diagnosis over IP
    :cvar PDU_R: Pdu Router
    :cvar UDP_NM: Udp Nm
    :cvar XCP: Universal Measurement and Calibration Protocol
    """

    DO_IP = "DO-IP"
    PDU_R = "PDU-R"
    UDP_NM = "UDP-NM"
    XCP = "XCP"
