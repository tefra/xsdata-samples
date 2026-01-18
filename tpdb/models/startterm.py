from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.automaton import Automaton
from tpdb.models.constructor_based import ConstructorBased
from tpdb.models.full import Full


@dataclass
class Startterm:
    class Meta:
        name = "startterm"

    constructor_based: None | ConstructorBased = field(
        default=None,
        metadata={
            "name": "constructor-based",
            "type": "Element",
        },
    )
    full: None | Full = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    automaton: None | Automaton = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
