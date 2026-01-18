from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class OrientEnumSimple(Enum):
    """
    :cvar LAND: This indicates that the table is rendered in landscape
        which results in turning the table 90 degree clockwise.
    :cvar PORT: This indicates that the table is rendered in portrait,
        which is the regular text flow.
    """

    LAND = "LAND"
    PORT = "PORT"
