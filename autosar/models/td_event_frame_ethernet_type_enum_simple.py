from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventFrameEthernetTypeEnumSimple(Enum):
    """
    :cvar FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION: A point in time where
        the Ethernet frame containing the specified PDUs is queued for
        transmission within the corresponding Ethernet Communication
        Driver.
    :cvar FRAME_ETHERNET_RECEIVED_BY_IF: A point in time where the frame
        is pushed from the corresponding Ethernet communication
        controller to the BSW Ethernet communication interface.
    :cvar FRAME_ETHERNET_RECEIVED_ON_BUS: A point in time where the
        receipt of the Ethernet frame/packet completes successfully on
        the recipient's Ethernet communication controller. In other
        words, the Ethernet frame/packet has entered the recipient's
        Ethernet communication controller which means the last bit of
        the Ethernet frame/packet has been received.
    :cvar FRAME_ETHERNET_SENT_ON_BUS: A point in time where the
        transmission of the Ethernet frame/packet completes successfully
        on the physical Ethernet communication network. In other words,
        the Ethernet frame/packet has left the sender's Ethernet
        communication controller, which means that the last bit of the
        Ethernet frame/packet has been sent.
    """
    FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION = "FRAME-ETHERNET-QUEUED-FOR-TRANSMISSION"
    FRAME_ETHERNET_RECEIVED_BY_IF = "FRAME-ETHERNET-RECEIVED-BY-IF"
    FRAME_ETHERNET_RECEIVED_ON_BUS = "FRAME-ETHERNET-RECEIVED-ON-BUS"
    FRAME_ETHERNET_SENT_ON_BUS = "FRAME-ETHERNET-SENT-ON-BUS"
