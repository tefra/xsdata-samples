from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.theory_value import TheoryValue


@dataclass
class Theory:
    class Meta:
        name = "theory"

    value: TheoryValue | None = field(default=None)
