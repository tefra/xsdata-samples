from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class TypeLoggingLevel2(Enum):
    """
    The type of various Logging levels.
    """
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
