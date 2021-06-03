from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EcucScopeEnumSimple(Enum):
    """
    :cvar ECU: An element may be shared with other modules.
    :cvar LOCAL: An element is only be applicable for the module it is
        defined in.
    """
    ECU = "ECU"
    LOCAL = "LOCAL"
