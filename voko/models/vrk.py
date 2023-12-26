from dataclasses import dataclass, field
from typing import List
from voko.models.url import Url


@dataclass(kw_only=True)
class Vrk:
    class Meta:
        name = "vrk"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "url",
                    "type": Url,
                },
            ),
        },
    )
