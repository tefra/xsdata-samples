from __future__ import annotations

from enum import StrEnum


class StrategyValue(StrEnum):
    FULL = "FULL"
    INNERMOST = "INNERMOST"
    OUTERMOST = "OUTERMOST"
