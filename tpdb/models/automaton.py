from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.automatonstuff import Automatonstuff


@dataclass
class Automaton:
    class Meta:
        name = "automaton"

    automatonstuff: Optional[Automatonstuff] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
