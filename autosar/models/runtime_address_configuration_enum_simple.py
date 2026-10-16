from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RuntimeAddressConfigurationEnumSimple(StrEnum):
    """
    :cvar NONE: Static configuration is used to obtain the address
        information.
    :cvar SD: AUTOSAR Service Discovery is used to obtain the address
        information.
    """

    NONE = "NONE"
    SD = "SD"
