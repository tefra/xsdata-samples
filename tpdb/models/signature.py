from dataclasses import dataclass, field
from typing import List

from tpdb.models.funcsym import Funcsym


@dataclass
class Signature:
    class Meta:
        name = "signature"

    funcsym: List[Funcsym] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
