from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.strategy_value import StrategyValue


@dataclass
class Strategy:
    class Meta:
        name = "strategy"

    value: Optional[StrategyValue] = field(default=None)
