from dataclasses import dataclass, field

from voko.models.ekz import Klr
from voko.models.tld import Tld


@dataclass(kw_only=True)
class Lstref:
    class Meta:
        name = "lstref"

    lst: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "tld",
                    "type": Tld,
                },
                {
                    "name": "klr",
                    "type": Klr,
                },
            ),
        },
    )
