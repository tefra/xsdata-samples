from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SeverityEnumSimple(Enum):
    """
    :cvar ERROR: Something is not right. High risk of interoperability
        issues.
    :cvar INFO: Something was found that is worth mentioning. Low risk
        of interoperability issues.
    :cvar WARNING: Something might be wrong depending on the context.
        Medium risk of interoperability issues.
    """
    ERROR = "ERROR"
    INFO = "INFO"
    WARNING = "WARNING"
