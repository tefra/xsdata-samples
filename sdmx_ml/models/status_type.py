from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


class StatusType(Enum):
    """
    StatusType provides an enumeration of values that detail the status of queries
    or requests.

    :cvar SUCCESS: Query or request successful.
    :cvar WARNING: Query or request successful, but with warnings.
    :cvar FAILURE: Query or request not successful.
    """

    SUCCESS = "Success"
    WARNING = "Warning"
    FAILURE = "Failure"
