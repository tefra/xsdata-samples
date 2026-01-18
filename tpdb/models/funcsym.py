from dataclasses import dataclass, field

from tpdb.models.arity import Arity
from tpdb.models.name import Name
from tpdb.models.replacementmap import Replacementmap
from tpdb.models.theory import Theory


@dataclass
class Funcsym:
    class Meta:
        name = "funcsym"

    name: Name | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arity: Arity | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    theory: Theory | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    replacementmap: Replacementmap | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
