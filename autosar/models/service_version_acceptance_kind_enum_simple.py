from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ServiceVersionAcceptanceKindEnumSimple(Enum):
    """
    :cvar EXACT_OR_ANY_MINOR_VERSION: Search for ANY or specific minor
        version service instance and select either ALL returned service
        instances (in case of ANY) or exactly the specific minor version
        service instances defined in requiredMinorVersion.
    :cvar MINIMUM_MINOR_VERSION: Search for ANY minor version service
        instance and select only those service instances which have an
        equal or greater minor version than given in
        requiredMinorVersion.
    """

    EXACT_OR_ANY_MINOR_VERSION = "EXACT-OR-ANY-MINOR-VERSION"
    MINIMUM_MINOR_VERSION = "MINIMUM-MINOR-VERSION"
