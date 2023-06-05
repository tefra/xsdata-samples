from dataclasses import dataclass, field
from typing import Optional
from voko.models.art import Art
from voko.models.parto import Parto
from voko.models.sekcio import Sekcio


@dataclass(kw_only=True)
class PrecipaParto:
    class Meta:
        name = "precipa-parto"

    parto: Optional[Parto] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sekcio: Optional[Sekcio] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    art: Optional[Art] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
