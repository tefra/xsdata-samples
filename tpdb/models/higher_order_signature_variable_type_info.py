from dataclasses import dataclass, field
from typing import List

from tpdb.models.var_declaration import VarDeclaration


@dataclass
class HigherOrderSignatureVariableTypeInfo:
    class Meta:
        global_type = False

    var_declaration: List[VarDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "varDeclaration",
            "type": "Element",
        },
    )
