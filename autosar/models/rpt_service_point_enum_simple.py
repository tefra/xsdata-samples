from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RptServicePointEnumSimple(Enum):
    """
    :cvar ENABLED: Enables generation of service points by the RTE
        generator.
    :cvar NONE: No Service Points are requested.
    """
    ENABLED = "ENABLED"
    NONE = "NONE"
