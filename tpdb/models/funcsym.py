from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.arity import Arity
from tpdb.models.name import Name
from tpdb.models.replacementmap import Replacementmap
from tpdb.models.theory import Theory


@dataclass(kw_only=True)
class Funcsym:
    class Meta:
        name = "funcsym"

    name: Name = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    arity: Arity = field(
        metadata={
            "type": "Element",
            "required": True,
        }
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
