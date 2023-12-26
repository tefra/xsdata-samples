from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ReportBehaviorEnumSimple(Enum):
    """
    :cvar REPORT_AFTER_INIT: This allows reporting related events after
        initialization
    :cvar REPORT_BEFORE_INIT: This allows reporting related events
        before initialization
    """

    REPORT_AFTER_INIT = "REPORT-AFTER-INIT"
    REPORT_BEFORE_INIT = "REPORT-BEFORE-INIT"
