from dataclasses import dataclass, field

from tpdb.models.type_mod import Type


@dataclass
class TypeDeclaration:
    class Meta:
        name = "typeDeclaration"

    type_value: list[Type] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "min_occurs": 1,
        },
    )
