from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ResumePositionSimple(Enum):
    """
    :cvar CONTINUE_AT_IT_POSITION: Continue at IT Point.
    :cvar START_FROM_BEGINNING: Start from the beginning
    """

    CONTINUE_AT_IT_POSITION = "CONTINUE-AT-IT-POSITION"
    START_FROM_BEGINNING = "START-FROM-BEGINNING"
