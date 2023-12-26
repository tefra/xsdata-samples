from dataclasses import dataclass, field
from typing import List
from voko.models.alineo import Alineo


@dataclass(kw_only=True)
class Epilogo:
    class Meta:
        name = "epilogo"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alineo",
                    "type": Alineo,
                },
            ),
        },
    )
