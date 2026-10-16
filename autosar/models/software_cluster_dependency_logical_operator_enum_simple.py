from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwareClusterDependencyLogicalOperatorEnumSimple(StrEnum):
    """
    :cvar LOGICAL_AND: logical and
    :cvar LOGICAL_OR: logical or
    """

    LOGICAL_AND = "LOGICAL-AND"
    LOGICAL_OR = "LOGICAL-OR"
