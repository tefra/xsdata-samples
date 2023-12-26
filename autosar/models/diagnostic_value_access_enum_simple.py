from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticValueAccessEnumSimple(Enum):
    """
    :cvar READ_ONLY: The access to the data element is limited to read-
        only. This is typically used to read-out diagnostic information
        (e.g. current values).
    :cvar READ_WRITE: The value of the diagnostic data element is
        classified as configurable (read and write access is possible).
    :cvar WRITE_ONLY: The access to the data element is limited to
        write-only. This supports the use case where the Dcm just writes
        data to the application software without the intention to read
        it back,
    """

    READ_ONLY = "READ-ONLY"
    READ_WRITE = "READ-WRITE"
    WRITE_ONLY = "WRITE-ONLY"
