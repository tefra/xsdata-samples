from dataclasses import dataclass, field

from voko.models.g import G
from voko.models.k import K


@dataclass(kw_only=True)
class Sup:
    class Meta:
        name = "sup"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "g",
                    "type": G,
                },
                {
                    "name": "k",
                    "type": K,
                },
            ),
        },
    )
