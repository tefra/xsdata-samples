from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OperatorActionOriginEnum(Enum):
    """
    Origins of operator actions.

    :cvar EXTERNAL: Operator action originated externally to the
        authority which is taking the action.
    :cvar INTERNAL: Operator action originated within the authority
        which is taking the action.
    """
    EXTERNAL = "external"
    INTERNAL = "internal"
