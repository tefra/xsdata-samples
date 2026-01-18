from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RptPreparationEnumSimple(Enum):
    """
    :cvar NONE: No RP preparation for VariableDataPrototype.
    :cvar RPT_LEVEL_1: The RTE implementation uses an „RP global buffer"
        for measurement and post-build hooking purposes.
    :cvar RPT_LEVEL_2: As rpLevel1 but the RTE implementation also uses
        both „RP enabler flag" to permit RP overwrite at run-time.
    :cvar RPT_LEVEL_3: As rpLevel2 but the RTE implementation also uses
        "RP global measurement buffer" to record the original ECU-
        generated value in addition to the RP value.
    """

    NONE = "NONE"
    RPT_LEVEL_1 = "RPT-LEVEL-1"
    RPT_LEVEL_2 = "RPT-LEVEL-2"
    RPT_LEVEL_3 = "RPT-LEVEL-3"
