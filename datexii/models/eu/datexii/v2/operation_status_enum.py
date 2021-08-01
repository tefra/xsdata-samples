from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OperationStatusEnum(Enum):
    """
    Specifies, whether some scenario or equipment is in operation or not.

    :cvar IN_OPERATION: The specified element is in operation right now.
    :cvar LIMITED_OPERATION: The specified element is in operation on a
        limited basis.
    :cvar NOT_IN_OPERATION: The specified element is not operating right
        now.
    :cvar NOT_IN_OPERATION_ABNORMAL: The specified element is not
        operating due to abnormal conditions (holidays, restoration-
        works, long-term closure, ....).
    :cvar TECHNICAL_DEFECT: The specified element is not in operation
        due to a technical defect.
    :cvar UNKNOWN: There is no information about the operation status.
    """
    IN_OPERATION = "inOperation"
    LIMITED_OPERATION = "limitedOperation"
    NOT_IN_OPERATION = "notInOperation"
    NOT_IN_OPERATION_ABNORMAL = "notInOperationAbnormal"
    TECHNICAL_DEFECT = "technicalDefect"
    UNKNOWN = "unknown"
