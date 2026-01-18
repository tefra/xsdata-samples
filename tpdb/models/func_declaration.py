from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.name import Name
from tpdb.models.type_declaration import TypeDeclaration


@dataclass
class FuncDeclaration:
    class Meta:
        name = "funcDeclaration"

    name: Name | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_declaration: TypeDeclaration | None = field(
        default=None,
        metadata={
            "name": "typeDeclaration",
            "type": "Element",
            "required": True,
        },
    )
