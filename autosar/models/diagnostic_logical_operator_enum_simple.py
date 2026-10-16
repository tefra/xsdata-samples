from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticLogicalOperatorEnumSimple(StrEnum):
    """
    :cvar LOGICAL_AND: Logical AND
    :cvar LOGICAL_OR: Logical OR
    """

    LOGICAL_AND = "LOGICAL-AND"
    LOGICAL_OR = "LOGICAL-OR"
