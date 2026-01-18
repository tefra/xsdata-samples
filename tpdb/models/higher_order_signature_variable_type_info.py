from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.var_declaration import VarDeclaration


@dataclass
class HigherOrderSignatureVariableTypeInfo:
    class Meta:
        global_type = False

    var_declaration: list[VarDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "varDeclaration",
            "type": "Element",
        },
    )
