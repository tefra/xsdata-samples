from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OpenlrFunctionalRoadClassEnum(Enum):
    """
    Enemuration of functional road class.

    :cvar FRC0: Main road, highest importance
    :cvar FRC1: First class road
    :cvar FRC2: Second class road
    :cvar FRC3: Third class road
    :cvar FRC4: Fourth class road
    :cvar FRC5: Fifth class road
    :cvar FRC6: Sixth class road
    :cvar FRC7: Other class road, lowest importance
    """

    FRC0 = "FRC0"
    FRC1 = "FRC1"
    FRC2 = "FRC2"
    FRC3 = "FRC3"
    FRC4 = "FRC4"
    FRC5 = "FRC5"
    FRC6 = "FRC6"
    FRC7 = "FRC7"
