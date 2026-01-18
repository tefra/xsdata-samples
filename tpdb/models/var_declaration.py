from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.type_mod import Type
from tpdb.models.var import Var


@dataclass
class VarDeclaration:
    class Meta:
        name = "varDeclaration"

    var: None | Var = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: None | Type = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
