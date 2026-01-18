from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.art import Art
from voko.models.parto import Parto
from voko.models.sekcio import Sekcio


@dataclass(kw_only=True)
class PrecipaParto:
    class Meta:
        name = "precipa-parto"

    parto: None | Parto = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sekcio: None | Sekcio = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    art: None | Art = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
