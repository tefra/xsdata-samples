from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataTransformationErrorHandlingEnumSimple(StrEnum):
    """
    :cvar NO_TRANSFORMER_ERROR_HANDLING: A runnable does not handle
        transformer errors.
    :cvar TRANSFORMER_ERROR_HANDLING: The runnable implements the
        handling of transformer errors.
    """

    NO_TRANSFORMER_ERROR_HANDLING = "NO-TRANSFORMER-ERROR-HANDLING"
    TRANSFORMER_ERROR_HANDLING = "TRANSFORMER-ERROR-HANDLING"
