from dataclasses import dataclass, field

from tpdb.models.automaton import Automaton
from tpdb.models.constructor_based import ConstructorBased
from tpdb.models.full import Full


@dataclass
class Startterm:
    class Meta:
        name = "startterm"

    constructor_based: ConstructorBased | None = field(
        default=None,
        metadata={
            "name": "constructor-based",
            "type": "Element",
        },
    )
    full: Full | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    automaton: Automaton | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
