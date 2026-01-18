from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.strategy_value import StrategyValue


@dataclass(kw_only=True)
class Strategy:
    class Meta:
        name = "strategy"

    value: StrategyValue = field()
