from dataclasses import dataclass, field
from typing import List
from voko.models.alineo import Alineo
from voko.models.autoro import Autoro
from voko.models.titolo import Titolo


@dataclass(kw_only=True)
class Prologo:
    class Meta:
        name = "prologo"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "titolo",
                    "type": Titolo,
                },
                {
                    "name": "autoro",
                    "type": Autoro,
                },
                {
                    "name": "alineo",
                    "type": Alineo,
                },
            ),
        },
    )
