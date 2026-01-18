from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.conditiontype_value import ConditiontypeValue


@dataclass(kw_only=True)
class Conditiontype:
    class Meta:
        name = "conditiontype"

    value: ConditiontypeValue = field()
