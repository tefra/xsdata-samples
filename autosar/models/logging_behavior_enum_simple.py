from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class LoggingBehaviorEnumSimple(StrEnum):
    """
    :cvar DOES_NOT_USE_LOGGING: The Executable indicates its intention
        to not use logging.
    :cvar USES_LOGGING: The Executable indicates its intention to use
        logging
    """

    DOES_NOT_USE_LOGGING = "DOES-NOT-USE-LOGGING"
    USES_LOGGING = "USES-LOGGING"
