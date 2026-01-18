from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.art import Art
from voko.models.epilogo import Epilogo
from voko.models.precipa_parto import PrecipaParto
from voko.models.prologo import Prologo


@dataclass(kw_only=True)
class Vortaro:
    class Meta:
        name = "vortaro"

    prologo: None | Prologo = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    precipa_parto: None | PrecipaParto = field(
        default=None,
        metadata={
            "name": "precipa-parto",
            "type": "Element",
        },
    )
    epilogo: None | Epilogo = field(
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
