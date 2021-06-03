from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticOccurrenceCounterProcessingEnumSimple(Enum):
    """
    :cvar CONFIRMED_DTC_BIT: The occurrence counter is triggered by the
        TestFailed bit if the fault confirmation was successful
        (ConfirmedDTC bit is set).
    :cvar TEST_FAILED_BIT: The occurrence counter is only triggered by
        the TestFailed bit (and the fault confirmation is not
        considered).
    """
    CONFIRMED_DTC_BIT = "CONFIRMED-DTC-BIT"
    TEST_FAILED_BIT = "TEST-FAILED-BIT"
