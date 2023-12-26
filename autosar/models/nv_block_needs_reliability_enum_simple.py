from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NvBlockNeedsReliabilityEnumSimple(Enum):
    """
    :cvar ERROR_CORRECTION: Errors shall be corrected
    :cvar ERROR_DETECTION: Errors shall be detected
    :cvar NO_PROTECTION: Data need not to be handled with protection
    """

    ERROR_CORRECTION = "ERROR-CORRECTION"
    ERROR_DETECTION = "ERROR-DETECTION"
    NO_PROTECTION = "NO-PROTECTION"
