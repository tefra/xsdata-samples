from dataclasses import dataclass, field
from typing import List

from voko.models.aut import Aut


@dataclass(kw_only=True)
class Adm:
    class Meta:
        name = "adm"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "aut",
                    "type": Aut,
                },
            ),
        },
    )
