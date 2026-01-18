from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.tld import Tld


@dataclass(kw_only=True)
class Ts:
    class Meta:
        name = "ts"

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
            ),
        },
    )
