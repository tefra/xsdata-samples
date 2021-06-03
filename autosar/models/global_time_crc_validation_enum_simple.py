from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class GlobalTimeCrcValidationEnumSimple(Enum):
    """
    :cvar CRC_IGNORED: The CRC is supposed to be ignored
    :cvar CRC_NOT_VALIDATED: The CRC is not supposed to be present. If
        CRC is present the message is ignored.
    :cvar CRC_OPTIONAL: Either the CRC is present and then shall be
        validated or the CRC is not present and no CRC check is done.
    :cvar CRC_VALIDATED: This CRC is supposed to be validated.
    """
    CRC_IGNORED = "CRC-IGNORED"
    CRC_NOT_VALIDATED = "CRC-NOT-VALIDATED"
    CRC_OPTIONAL = "CRC-OPTIONAL"
    CRC_VALIDATED = "CRC-VALIDATED"
