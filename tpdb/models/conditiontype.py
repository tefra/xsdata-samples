from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.conditiontype_value import ConditiontypeValue


@dataclass
class Conditiontype:
    class Meta:
        name = "conditiontype"

    value: None | ConditiontypeValue = field(default=None)
