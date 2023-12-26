from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class LogTraceDefaultLogLevelEnumSimple(Enum):
    """
    :cvar DEBUG: Detailed information for programmers
    :cvar ERROR: Error with impact to correct functionality
    :cvar FATAL: Fatal error
    :cvar INFO: High level information
    :cvar VERBOSE: Verbose debug message
    :cvar WARN: Warning if correct behavior cannot be ensured
    """

    DEBUG = "DEBUG"
    ERROR = "ERROR"
    FATAL = "FATAL"
    INFO = "INFO"
    VERBOSE = "VERBOSE"
    WARN = "WARN"
