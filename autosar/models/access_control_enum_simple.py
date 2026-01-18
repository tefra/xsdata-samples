from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AccessControlEnumSimple(Enum):
    """
    :cvar CUSTOM: The access restriction to the resource is defined by a
        non-AUTOSAR process.
    :cvar MODELED: The access restriction to the resource is modeled in
        the AUTOSAR Application Design model or the AUTOSAR Deployment
        model.
    """

    CUSTOM = "CUSTOM"
    MODELED = "MODELED"
