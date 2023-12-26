from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HandleInvalidEnumSimple(Enum):
    """
    :cvar DONT_INVALIDATE: Invalidation is switched off.
    :cvar EXTERNAL_REPLACEMENT: Replace a received invalidValue. The
        replacement value is sourced from the externalReplacement.
    :cvar KEEP: The application software is supposed to  handle signal
        invalidation on RTE API level either by DataReceiveErrorEvent or
        check of error code on read access.
    :cvar REPLACE: Replace a received invalidValue. The replacement
        value is specified by the initValue.
    """

    DONT_INVALIDATE = "DONT-INVALIDATE"
    EXTERNAL_REPLACEMENT = "EXTERNAL-REPLACEMENT"
    KEEP = "KEEP"
    REPLACE = "REPLACE"
