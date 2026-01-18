from dataclasses import dataclass, field

from voko.models.art import Art


@dataclass(kw_only=True)
class Sekcio:
    class Meta:
        name = "sekcio"

    lit: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    art: list[Art] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
