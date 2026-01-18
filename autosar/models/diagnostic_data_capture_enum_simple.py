from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticDataCaptureEnumSimple(Enum):
    """
    :cvar CAPTURE_ASYNCHRONOUSLY_TO_REPORTING: This represents the
        intention to capture the environment data asynchronously after
        the actual capture API function terminated.
    :cvar CAPTURE_SYNCHRONOUSLY_TO_REPORTING: This represents the
        intention to capture the environment data synchronously within
        the capture API function.
    """

    CAPTURE_ASYNCHRONOUSLY_TO_REPORTING = "CAPTURE-ASYNCHRONOUSLY-TO-REPORTING"
    CAPTURE_SYNCHRONOUSLY_TO_REPORTING = "CAPTURE-SYNCHRONOUSLY-TO-REPORTING"
