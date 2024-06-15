from dataclasses import dataclass, field
from typing import List

from tpdb.models.func_declaration import FuncDeclaration


@dataclass
class HigherOrderSignatureFunctionSymbolTypeInfo:
    class Meta:
        global_type = False

    func_declaration: List[FuncDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "funcDeclaration",
            "type": "Element",
        },
    )
