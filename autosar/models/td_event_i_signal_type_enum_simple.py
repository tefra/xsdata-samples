from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventISignalTypeEnumSimple(Enum):
    """
    :cvar I_SIGNAL_AVAILABLE_FOR_RTE: A point in time, where the COM
        module makes the contained signal / signal group available for
        the RTE and the corresponding Rx Indication callout is generated
        (if configured).
    :cvar I_SIGNAL_SENT_TO_COM: A point in time, where a transmission
        request call is issued by the RTE on a named COM signal / signal
        group and the new value is stored to the carrier COM I-PDU
        buffer.
    """
    I_SIGNAL_AVAILABLE_FOR_RTE = "I-SIGNAL-AVAILABLE-FOR-RTE"
    I_SIGNAL_SENT_TO_COM = "I-SIGNAL-SENT-TO-COM"
