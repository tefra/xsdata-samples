from dataclasses import dataclass, field
from typing import List

from tpdb.models.type_mod import TypeType


@dataclass
class TypeDeclaration:
    class Meta:
        name = "typeDeclaration"

    type_value: List[TypeType] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "min_occurs": 1,
        },
    )
