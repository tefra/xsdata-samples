from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.name import Name
from tpdb.models.type_declaration import TypeDeclaration


@dataclass(kw_only=True)
class FuncDeclaration:
    class Meta:
        name = "funcDeclaration"

    name: Name = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_declaration: TypeDeclaration = field(
        metadata={
            "name": "typeDeclaration",
            "type": "Element",
            "required": True,
        }
    )
