from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.funcsym import Funcsym


@dataclass
class Signature:
    class Meta:
        name = "signature"

    funcsym: list[Funcsym] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
