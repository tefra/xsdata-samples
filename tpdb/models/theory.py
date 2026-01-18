from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.theory_value import TheoryValue


@dataclass(kw_only=True)
class Theory:
    class Meta:
        name = "theory"

    value: TheoryValue = field()
