from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RuntimeAddressConfigurationEnumSimple(Enum):
    """
    :cvar NONE: Static configuration is used to obtain the address
        information.
    :cvar SD: AUTOSAR Service Discovery is used to obtain the address
        information.
    """

    NONE = "NONE"
    SD = "SD"
