from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventFrameTypeEnumSimple(Enum):
    """
    :cvar FRAME_QUEUED_FOR_TRANSMISSION: A point in time where the frame
        containing the named signal / I-PDU is queued for transmission
        within the related Communication Driver.
    :cvar FRAME_RECEIVED_BY_IF: A point in time where the frame is
        pushed from the subscriber's communication controller to the
        corresponding (FlexRay / CAN / LIN) Interface BSW module.
    :cvar FRAME_TRANSMITTED_ON_BUS: A point in time where the
        transmission of the frame completes successfully, and the
        subscriber's communication controller receives the frame from
        the bus.
    """
    FRAME_QUEUED_FOR_TRANSMISSION = "FRAME-QUEUED-FOR-TRANSMISSION"
    FRAME_RECEIVED_BY_IF = "FRAME-RECEIVED-BY-IF"
    FRAME_TRANSMITTED_ON_BUS = "FRAME-TRANSMITTED-ON-BUS"
