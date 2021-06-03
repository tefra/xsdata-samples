from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventIPduTypeEnumSimple(Enum):
    """
    :cvar I_PDU_RECEIVED_BY_COM: A point in time where the received
        frame is processed by the corresponding (FlexRay / CAN / LIN)
        Interface BSW module, routed through the PDUR and the contained
        PDUs are pushed to the COM module.
    :cvar I_PDU_SENT_TO_IF: A point in time where the carrier COM I-PDU
        is routed through the PDUR and is pushed to the bus specific
        (FlexRay / CAN / LIN) Interface BSW module.
    """
    I_PDU_RECEIVED_BY_COM = "I-PDU-RECEIVED-BY-COM"
    I_PDU_SENT_TO_IF = "I-PDU-SENT-TO-IF"
