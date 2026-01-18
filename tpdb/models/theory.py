from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.theory_value import TheoryValue


@dataclass
class Theory:
    class Meta:
        name = "theory"

    value: TheoryValue | None = field(default=None)
