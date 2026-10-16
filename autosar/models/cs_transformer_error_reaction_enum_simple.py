from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CsTransformerErrorReactionEnumSimple(StrEnum):
    """
    :cvar APPLICATION_ONLY: The application is responsible for any error
        reaction. No autonomous error reaction of RTE and transformer.
    :cvar AUTONOMOUS: RTE and Transformer coordinate an autonomous error
        reaction on their own.
    """

    APPLICATION_ONLY = "APPLICATION-ONLY"
    AUTONOMOUS = "AUTONOMOUS"
