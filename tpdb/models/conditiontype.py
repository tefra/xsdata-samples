from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.conditiontype_value import ConditiontypeValue


@dataclass
class Conditiontype:
    class Meta:
        name = "conditiontype"

    value: ConditiontypeValue | None = field(default=None)
