from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ObdRatioConnectionKindEnumSimple(Enum):
    """
    :cvar API_USE: The IUMPR service (of the DEM) uses an explicit API
        to connect to the component or module.
    :cvar OBSERVER: The IUMPR service (of the Dem) uses no API but
        "observes"  the associated diagnostic event.
    """

    API_USE = "API-USE"
    OBSERVER = "OBSERVER"
