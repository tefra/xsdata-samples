from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticRecordTriggerEnumSimple(Enum):
    """
    :cvar CONFIRMED: capture on "Confirmed"
    :cvar CUSTOM: implement custom capture
    :cvar FDC_THRESHOLD: capture on "FDC Threshold"
    :cvar PENDING: capture on "Pending"
    :cvar TEST_FAILED: capture on "Test Failed"
    :cvar TEST_FAILED_THIS_OPERATION_CYCLE: Test Failed This Operation
        Cycle.
    """

    CONFIRMED = "CONFIRMED"
    CUSTOM = "CUSTOM"
    FDC_THRESHOLD = "FDC-THRESHOLD"
    PENDING = "PENDING"
    TEST_FAILED = "TEST-FAILED"
    TEST_FAILED_THIS_OPERATION_CYCLE = "TEST-FAILED-THIS-OPERATION-CYCLE"
