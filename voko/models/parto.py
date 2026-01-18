from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.art import Art
from voko.models.sekcio import Sekcio


@dataclass(kw_only=True)
class Parto:
    class Meta:
        name = "parto"

    lng: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
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
