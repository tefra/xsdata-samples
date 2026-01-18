from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class FuelType2Enum(Enum):
    """
    Fuel types that are currently not supported in FuelTypeEnum.

    :cvar ALL: All sort of fuel is accepted.
    :cvar PETROL95_OCTANE: Petrol with 95 octane.
    :cvar PETROL98_OCTANE: Petrol with 98 octane.
    :cvar PETROL_LEADED: Leaded petrol.
    :cvar PETROL_UNLEADED: Unleaded petrol.
    :cvar UNKNOWN: The sort of fuel is not known.
    :cvar OTHER: Other.
    """

    ALL = "all"
    PETROL95_OCTANE = "petrol95Octane"
    PETROL98_OCTANE = "petrol98Octane"
    PETROL_LEADED = "petrolLeaded"
    PETROL_UNLEADED = "petrolUnleaded"
    UNKNOWN = "unknown"
    OTHER = "other"
