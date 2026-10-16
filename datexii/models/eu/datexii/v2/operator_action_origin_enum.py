from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OperatorActionOriginEnum(StrEnum):
    """
    Origins of operator actions.

    :cvar EXTERNAL: Operator action originated externally to the
        authority which is taking the action.
    :cvar INTERNAL: Operator action originated within the authority
        which is taking the action.
    """

    EXTERNAL = "external"
    INTERNAL = "internal"
