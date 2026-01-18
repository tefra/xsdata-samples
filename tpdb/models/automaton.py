from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.automatonstuff import Automatonstuff


@dataclass
class Automaton:
    class Meta:
        name = "automaton"

    automatonstuff: None | Automatonstuff = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
