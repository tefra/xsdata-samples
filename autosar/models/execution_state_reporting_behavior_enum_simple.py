from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ExecutionStateReportingBehaviorEnumSimple(Enum):
    """
    :cvar DOES_NOT_REPORT_EXECUTION_STATE: The Executable shall not
        report its execution state to the Execution Management.
    :cvar REPORTS_EXECUTION_STATE: The Executable shall report its
        execution state to the Execution Management.
    """

    DOES_NOT_REPORT_EXECUTION_STATE = "DOES-NOT-REPORT-EXECUTION-STATE"
    REPORTS_EXECUTION_STATE = "REPORTS-EXECUTION-STATE"
