from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticClearDtcLimitationEnumSimple(Enum):
    """
    :cvar ALL_SUPPORTED_DTCS: DEM_ClearDtc API accepts all supported DTC
        values.
    :cvar CLEAR_ALL_DTCS: DEM_ClearDtc API accepts ClearAllDTCs only.
    """
    ALL_SUPPORTED_DTCS = "ALL-SUPPORTED-DTCS"
    CLEAR_ALL_DTCS = "CLEAR-ALL-DTCS"
