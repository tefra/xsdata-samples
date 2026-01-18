from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TransformerClassEnumSimple(Enum):
    """
    :cvar CUSTOM: The transformer is a custom transformer.
    :cvar SAFETY: The transformer is a safety transformer.
    :cvar SECURITY: The transformer is a security transformer.
    :cvar SERIALIZER: The transformer is a serializing transformer.
    """

    CUSTOM = "CUSTOM"
    SAFETY = "SAFETY"
    SECURITY = "SECURITY"
    SERIALIZER = "SERIALIZER"
