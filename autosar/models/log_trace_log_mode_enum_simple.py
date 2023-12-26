from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class LogTraceLogModeEnumSimple(Enum):
    """
    :cvar CONSOLE: Destination of log message will be the console
        output.
    :cvar FILE: Destination of log message will be a file on the file
        system.
    :cvar NETWORK: Log message will be transmitted over the
        communication bus.
    """

    CONSOLE = "CONSOLE"
    FILE = "FILE"
    NETWORK = "NETWORK"
