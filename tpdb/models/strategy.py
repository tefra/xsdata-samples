from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.strategy_value import StrategyValue


@dataclass
class Strategy:
    class Meta:
        name = "strategy"

    value: StrategyValue | None = field(default=None)
