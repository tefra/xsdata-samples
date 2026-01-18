from dataclasses import dataclass, field

from voko.models.art import Art
from voko.models.parto import Parto
from voko.models.sekcio import Sekcio


@dataclass(kw_only=True)
class PrecipaParto:
    class Meta:
        name = "precipa-parto"

    parto: Parto | None = field(
        default=None,
        metadata={
            "type": "Element",
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
