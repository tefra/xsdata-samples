from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.type_mod import Type
from tpdb.models.var import Var


@dataclass
class VarDeclaration:
    class Meta:
        name = "varDeclaration"

    var: Optional[Var] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[Type] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
