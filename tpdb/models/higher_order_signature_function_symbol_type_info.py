from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.func_declaration import FuncDeclaration


@dataclass
class HigherOrderSignatureFunctionSymbolTypeInfo:
    class Meta:
        global_type = False

    func_declaration: list[FuncDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "funcDeclaration",
            "type": "Element",
        },
    )
