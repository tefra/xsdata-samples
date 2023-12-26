from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ElaboratedDataFaultEnum(Enum):
    """
    Types of elaborated data faults.

    :cvar INTERMITTENT_DATA_VALUES: Data values are being produced at
        intermittent intervals which are not consitent with the expected
        reporting interval.
    :cvar NO_DATA_VALUES_AVAILABLE: No elaborated data values are
        currently available.
    :cvar SPURIOUS_UNRELIABLE_DATA_VALUES: Spurious or unreliable data
        values are being produced.
    :cvar UNSPECIFIED_OR_UNKNOWN_FAULT: An unspecified or unknown fault
        exists in the process which is generating elaborated data.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    INTERMITTENT_DATA_VALUES = "intermittentDataValues"
    NO_DATA_VALUES_AVAILABLE = "noDataValuesAvailable"
    SPURIOUS_UNRELIABLE_DATA_VALUES = "spuriousUnreliableDataValues"
    UNSPECIFIED_OR_UNKNOWN_FAULT = "unspecifiedOrUnknownFault"
    OTHER = "other"
