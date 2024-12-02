from dataclasses import dataclass, field

from voko.models.url import Url


@dataclass(kw_only=True)
class Lok:
    class Meta:
        name = "lok"

    content: list[object] = field(
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
