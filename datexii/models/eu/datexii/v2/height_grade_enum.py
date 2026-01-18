from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class HeightGradeEnum(Enum):
    """
    List of height or vertical gradings of road sections.

    :cvar ABOVE_GRADE: Above or over the normal road grade elevation.
    :cvar AT_GRADE: At the normal road grade elevation.
    :cvar BELOW_GRADE: Below or under the normal road grade elevation.
    """

    ABOVE_GRADE = "aboveGrade"
    AT_GRADE = "atGrade"
    BELOW_GRADE = "belowGrade"
