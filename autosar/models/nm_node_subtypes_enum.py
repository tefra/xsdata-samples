from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NmNodeSubtypesEnum(Enum):
    CAN_NM_NODE = "CAN-NM-NODE"
    FLEXRAY_NM_NODE = "FLEXRAY-NM-NODE"
    J_1939_NM_NODE = "J-1939-NM-NODE"
    NM_NODE = "NM-NODE"
    UDP_NM_NODE = "UDP-NM-NODE"
