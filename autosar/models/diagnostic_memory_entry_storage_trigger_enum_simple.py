from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticMemoryEntryStorageTriggerEnumSimple(Enum):
    """
    :cvar CONFIRMED: Status information of UDS DTC status bit 3
    :cvar FDC_THRESHOLD: Threshold to allocate an event memory entry and
        to capture the Freeze Frame.
    :cvar PENDING: Status information of UDS DTC status bit 2.
    :cvar TEST_FAILED: Status information of UDS DTC status bit 0.
    """

    CONFIRMED = "CONFIRMED"
    FDC_THRESHOLD = "FDC-THRESHOLD"
    PENDING = "PENDING"
    TEST_FAILED = "TEST-FAILED"
