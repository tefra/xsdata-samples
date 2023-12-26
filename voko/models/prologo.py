from dataclasses import dataclass, field
from typing import List
from voko.models.alineo import Alineo


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
                    "type": str,
                },
                {
                    "name": "autoro",
                    "type": str,
                },
                {
                    "name": "alineo",
                    "type": Alineo,
                },
            ),
        },
    )
