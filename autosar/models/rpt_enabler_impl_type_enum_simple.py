from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RptEnablerImplTypeEnumSimple(Enum):
    """
    :cvar NONE: No "RP enabler" is implemented.
    :cvar RPT_ENABLER_RAM: "RP enabler" is implemented as a RAM variable
    :cvar RPT_ENABLER_RAM_AND_ROM: The RTE generator implements both the
        RAM and ROM "RP enabler".
    :cvar RPT_ENABLER_ROM: "RP enabler" is implemented as a
        calibrateable ROM variable.
    """

    NONE = "NONE"
    RPT_ENABLER_RAM = "RPT-ENABLER-RAM"
    RPT_ENABLER_RAM_AND_ROM = "RPT-ENABLER-RAM-AND-ROM"
    RPT_ENABLER_ROM = "RPT-ENABLER-ROM"
