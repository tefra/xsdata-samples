from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.arity import Arity
from tpdb.models.name import Name
from tpdb.models.replacementmap import Replacementmap
from tpdb.models.theory import Theory


@dataclass
class Funcsym:
    class Meta:
        name = "funcsym"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arity: Optional[Arity] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    theory: Optional[Theory] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    replacementmap: Optional[Replacementmap] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
