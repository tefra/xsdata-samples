from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventVariableDataPrototypeTypeEnumSimple(Enum):
    """
    :cvar VARIABLE_DATA_PROTOTYPE_RECEIVED: A point in time where the
        referenced variable data prototype has been successfully
        transmitted and is available in the related communication buffer
        (of the RTE) for the receiving SWC.
    :cvar VARIABLE_DATA_PROTOTYPE_SENT: A point in time where the
        referenced variable data prototype has been successfully sent
        out by the sending SWC, so that it is available in the related
        communication buffer (of the RTE) for transmission.
    """

    VARIABLE_DATA_PROTOTYPE_RECEIVED = "VARIABLE-DATA-PROTOTYPE-RECEIVED"
    VARIABLE_DATA_PROTOTYPE_SENT = "VARIABLE-DATA-PROTOTYPE-SENT"
