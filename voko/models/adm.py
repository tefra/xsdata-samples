from dataclasses import dataclass, field

from voko.models.aut import Aut


@dataclass(kw_only=True)
class Adm:
    class Meta:
        name = "adm"

    content: list[object] = field(
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
