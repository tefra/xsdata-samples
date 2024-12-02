from dataclasses import dataclass, field

from voko.models.vspec import Vspec


@dataclass(kw_only=True)
class Gra:
    class Meta:
        name = "gra"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "vspec",
                    "type": Vspec,
                },
            ),
        },
    )
