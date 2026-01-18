from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.type_mod import Type
from tpdb.models.var import Var


@dataclass(kw_only=True)
class VarDeclaration:
    class Meta:
        name = "varDeclaration"

    var: Var = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: Type = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
