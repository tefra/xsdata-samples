from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SomeipTransformerSessionHandlingEnumSimple(StrEnum):
    """
    :cvar SESSION_HANDLING_ACTIVE: The SOME/IP Transformer shall use
        session handling
    :cvar SESSION_HANDLING_INACTIVE: The SOME/IP Transformer doesn't use
        session handling
    """

    SESSION_HANDLING_ACTIVE = "SESSION-HANDLING-ACTIVE"
    SESSION_HANDLING_INACTIVE = "SESSION-HANDLING-INACTIVE"
