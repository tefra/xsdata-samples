from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class StandardNameEnumSimple(Enum):
    """
    :cvar AP: This values represents the Adaptive Platform.
    :cvar CP: This Value represents the Classic Platform.
    :cvar FO: This values represents the Foundation.
    :cvar TA: This Values represents the Testing of the Adaptive
        Platform.
    :cvar TC: This values represents the Testing of the Classic
        Platform.
    """
    AP = "AP"
    CP = "CP"
    FO = "FO"
    TA = "TA"
    TC = "TC"
