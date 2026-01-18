from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EnvironmentCaptureToReportingEnumSimple(Enum):
    """
    :cvar CAPTURE_ASYNCHRONOUS_TO_REPORTING: The data capturing is
        postponed to the next cycle of the Dem_Mainfunction. (This means
        that there is a minimum delay between report of the failure and
        capturing the data.
    :cvar CAPTURE_SYNCHRONOUS_TO_REPORTING: The data is captured
        immediately within the reporting function (i.e. in the context
        of the setEventStatus/reportErrorStatus function).
    """

    CAPTURE_ASYNCHRONOUS_TO_REPORTING = "CAPTURE-ASYNCHRONOUS-TO-REPORTING"
    CAPTURE_SYNCHRONOUS_TO_REPORTING = "CAPTURE-SYNCHRONOUS-TO-REPORTING"
