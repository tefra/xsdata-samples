from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HandleOutOfRangeEnumSimple(Enum):
    """
    :cvar DEFAULT: The RTE will use the initValue if the actual value is
        out of the specified bounds.
    :cvar EXTERNAL_REPLACEMENT: This indicates that the value
        replacement is sourced from the attribute replaceWith.
    :cvar IGNORE: The RTE will ignore any attempt to send or receive the
        corresponding dataElement if the value is out of the specified
        range.
    :cvar INVALID: The RTE will use the invalidValue if the value is out
        of the specified bounds.
    :cvar NONE: A range check is not required.
    :cvar SATURATE: The RTE will saturate the value of the dataElement
        such that it is limited to the applicable upper bound if it is
        greater than the upper bound. Consequently, it is limited to the
        applicable lower bound if the value is less than the lower
        bound.
    """

    DEFAULT = "DEFAULT"
    EXTERNAL_REPLACEMENT = "EXTERNAL-REPLACEMENT"
    IGNORE = "IGNORE"
    INVALID = "INVALID"
    NONE = "NONE"
    SATURATE = "SATURATE"
