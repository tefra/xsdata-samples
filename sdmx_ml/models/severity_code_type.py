from enum import Enum

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer"
)


class SeverityCodeType(Enum):
    """
    :cvar ERROR: Error indicates the status message coresponds to an
        error.
    :cvar WARNING: Warning indicates that the status message corresponds
        to a warning.
    :cvar INFORMATION: Information indicates that the status message
        corresponds to an informational message.
    """

    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"
