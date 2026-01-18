from dataclasses import dataclass, field

from voko.models.art import Art
from voko.models.sekcio import Sekcio


@dataclass(kw_only=True)
class Parto:
    class Meta:
        name = "parto"

    lng: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sekcio: Sekcio | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    art: Art | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
