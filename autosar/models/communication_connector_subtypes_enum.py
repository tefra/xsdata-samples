from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CommunicationConnectorSubtypesEnum(Enum):
    ABSTRACT_CAN_COMMUNICATION_CONNECTOR = "ABSTRACT-CAN-COMMUNICATION-CONNECTOR"
    CAN_COMMUNICATION_CONNECTOR = "CAN-COMMUNICATION-CONNECTOR"
    COMMUNICATION_CONNECTOR = "COMMUNICATION-CONNECTOR"
    ETHERNET_COMMUNICATION_CONNECTOR = "ETHERNET-COMMUNICATION-CONNECTOR"
    FLEXRAY_COMMUNICATION_CONNECTOR = "FLEXRAY-COMMUNICATION-CONNECTOR"
    LIN_COMMUNICATION_CONNECTOR = "LIN-COMMUNICATION-CONNECTOR"
    TTCAN_COMMUNICATION_CONNECTOR = "TTCAN-COMMUNICATION-CONNECTOR"
    USER_DEFINED_COMMUNICATION_CONNECTOR = "USER-DEFINED-COMMUNICATION-CONNECTOR"