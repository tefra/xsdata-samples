from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.arity import Arity
from tpdb.models.name import Name
from tpdb.models.replacementmap import Replacementmap
from tpdb.models.theory import Theory


@dataclass
class Funcsym:
    class Meta:
        name = "funcsym"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arity: None | Arity = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    theory: None | Theory = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    replacementmap: None | Replacementmap = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
