from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CouplingPortRoleEnumSimple(Enum):
    """
    :cvar HOST_PORT: The hostPort is connected to an ECU (host ecu). The
        host ECU controls the connected CouplingElement (e.g. Ethernet
        switch).
    :cvar STANDARD_PORT: A CoupingPort can be a standardPort that is
        used to connect the CouplingElement with CouplingPorts outside
        the ECU.
    :cvar UP_LINK_PORT: A CouplingPort can be connected to another
        CouplingPort of a CouplingElement located on the same ECU
        (CouplingElement.ecuInstance) using the CouplingPortConnection.
        This is used to model a cascaded switch.
    """

    HOST_PORT = "HOST-PORT"
    STANDARD_PORT = "STANDARD-PORT"
    UP_LINK_PORT = "UP-LINK-PORT"
