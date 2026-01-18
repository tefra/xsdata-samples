from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.automatonstuff import Automatonstuff


@dataclass(kw_only=True)
class Automaton:
    class Meta:
        name = "automaton"

    automatonstuff: Automatonstuff = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
