from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PncGatewayTypeEnumSimple(Enum):
    """
    :cvar ACTIVE: The active PncGateway functionality shall be performed
    :cvar NONE: No PncGateway functionality shall be performed
    :cvar PASSIVE: The passive PncGateway functionality shall be
        performed
    """

    ACTIVE = "ACTIVE"
    NONE = "NONE"
    PASSIVE = "PASSIVE"
