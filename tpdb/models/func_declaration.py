from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.name import Name
from tpdb.models.type_declaration import TypeDeclaration


@dataclass
class FuncDeclaration:
    class Meta:
        name = "funcDeclaration"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_declaration: None | TypeDeclaration = field(
        default=None,
        metadata={
            "name": "typeDeclaration",
            "type": "Element",
            "required": True,
        },
    )
