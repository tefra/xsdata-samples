from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SupportBufferLockingEnumSimple(Enum):
    """
    :cvar DOES_NOT_SUPPORT_BUFFER_LOCKING: Buffer locking is not
        supported.
    :cvar SUPPORTS_BUFFER_LOCKING: Buffer locking is supported.
    """

    DOES_NOT_SUPPORT_BUFFER_LOCKING = "DOES-NOT-SUPPORT-BUFFER-LOCKING"
    SUPPORTS_BUFFER_LOCKING = "SUPPORTS-BUFFER-LOCKING"
