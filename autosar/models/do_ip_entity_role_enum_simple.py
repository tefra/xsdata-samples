from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DoIpEntityRoleEnumSimple(Enum):
    """
    :cvar EDGE_NODE: Network node is a DoIP gateway that accepts
        external connections.
    :cvar GATEWAY: Network node is a Gateway between the DoIP network
        and other networks.
    :cvar NODE: Network node is a DoIp node.
    """
    EDGE_NODE = "EDGE-NODE"
    GATEWAY = "GATEWAY"
    NODE = "NODE"
