from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EndToEndProfileBehaviorEnumSimple(Enum):
    """
    :cvar PRE_R_4_2: Check has the legacy behavior, before AUTOSAR
        Release 4.2.
    :cvar R_4_2: Check behaves like new P4/P5/P6 profiles introduced in
        AUTOSAR Release 4.2.
    """

    PRE_R_4_2 = "PRE--R-4--2"
    R_4_2 = "R-4--2"
