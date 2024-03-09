from dataclasses import dataclass, field
from typing import Optional

from voko.models.art import Art
from voko.models.sekcio import Sekcio


@dataclass(kw_only=True)
class Parto:
    class Meta:
        name = "parto"

    lng: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sekcio: Optional[Sekcio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    art: Optional[Art] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
