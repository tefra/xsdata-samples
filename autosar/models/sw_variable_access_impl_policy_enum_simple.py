from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwVariableAccessImplPolicyEnumSimple(Enum):
    """
    :cvar DIRECT: Messages with DIRECT access are read but ignored by
        data consistency tool. Data consistency is not guaranteed.
    :cvar OPTIMIZED: A Tool handles data consistency. In SwService,
        where a message is referenced, only OPTIMIZED access (also
        default value inside SwServcie) is possible.
    :cvar SELECTABLE: The user can decide inside each single service,
        where these message is referenced, if access to that shall be
        OPTIMIZED or DIRECT.
    """
    DIRECT = "DIRECT"
    OPTIMIZED = "OPTIMIZED"
    SELECTABLE = "SELECTABLE"
