from dataclasses import dataclass, field
from typing import Optional

from voko.models.art import Art
from voko.models.epilogo import Epilogo
from voko.models.precipa_parto import PrecipaParto
from voko.models.prologo import Prologo


@dataclass(kw_only=True)
class Vortaro:
    class Meta:
        name = "vortaro"

    prologo: Prologo | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    precipa_parto: PrecipaParto | None = field(
        default=None,
        metadata={
            "name": "precipa-parto",
            "type": "Element",
        },
    )
    epilogo: Epilogo | None = field(
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
