from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HandleTimeoutEnumSimple(Enum):
    """
    :cvar NONE: If set to none no replacement shall take place.
    :cvar REPLACE: If set to replace, the replacement value shall be the
        ComInitValue.
    :cvar REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE: If set to replace, the
        replacement value shall be the timeout substitution value.
    """

    NONE = "NONE"
    REPLACE = "REPLACE"
    REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE = (
        "REPLACE-BY-TIMEOUT-SUBSTITUTION-VALUE"
    )
