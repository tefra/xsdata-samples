from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FmFeatureSelectionStateSimple(StrEnum):
    """
    :cvar DESELECTED: The feature is excluded from the selection.
    :cvar SELECTED: The feature is included in the selection.
    :cvar UNDECIDED: It is not yet decided whether the feature shall be
        included into or excluded from the selection.
    """

    DESELECTED = "DESELECTED"
    SELECTED = "SELECTED"
    UNDECIDED = "UNDECIDED"
