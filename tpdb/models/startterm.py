from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.automaton import Automaton
from tpdb.models.constructor_based import ConstructorBased
from tpdb.models.full import Full


@dataclass
class Startterm:
    class Meta:
        name = "startterm"

    constructor_based: Optional[ConstructorBased] = field(
        default=None,
        metadata={
            "name": "constructor-based",
            "type": "Element",
        },
    )
    full: Optional[Full] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    automaton: Optional[Automaton] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
