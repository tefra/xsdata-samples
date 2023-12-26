from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FilterDebouncingEnumSimple(Enum):
    """
    :cvar DEBOUNCE_DATA: The signal is a mean value
    :cvar RAW_DATA: Means that no modification of the signal has been
        applied. This is the default value
    :cvar WAIT_TIME_DATE: The signal is delivered by a GET operation
        after a certain amount of time
    """

    DEBOUNCE_DATA = "DEBOUNCE-DATA"
    RAW_DATA = "RAW-DATA"
    WAIT_TIME_DATE = "WAIT-TIME-DATE"
