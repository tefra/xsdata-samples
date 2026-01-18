from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SignalServiceTranslationControlEnumSimple(Enum):
    """
    :cvar PARTIAL_NETWORK: Defines the start of service control when
        specific partial networks are active.
    :cvar SERVICE_DISCOVERY: Defines the start of service control when
        other service is available.
    :cvar TRANSLATION_START: Defines the start of service control at
        translation start.
    """

    PARTIAL_NETWORK = "PARTIAL-NETWORK"
    SERVICE_DISCOVERY = "SERVICE-DISCOVERY"
    TRANSLATION_START = "TRANSLATION-START"
