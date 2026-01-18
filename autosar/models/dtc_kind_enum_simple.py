from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DtcKindEnumSimple(Enum):
    """
    :cvar EMISSION_RELATED_DTC: This indicates that the monitor reports
        a OBD-relevant malfunction.
    :cvar NON_EMMISSION_RELATED_DTC: This indicates that the monitor
        reports a non-OBD-relevant malfunction.
    """

    EMISSION_RELATED_DTC = "EMISSION-RELATED-DTC"
    NON_EMMISSION_RELATED_DTC = "NON-EMMISSION-RELATED-DTC"
