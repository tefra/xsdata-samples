from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RptAccessEnumSimple(Enum):
    """
    :cvar ENABLED: The related data element is accessible by RP tool.
    :cvar NONE: The related data element is not accessible by RP tool.
    :cvar PROTECTED: The data element is known to the RP tool however
        its usage for RP can be restricted. Use case: limitation based
        on access rights
    """

    ENABLED = "ENABLED"
    NONE = "NONE"
    PROTECTED = "PROTECTED"
