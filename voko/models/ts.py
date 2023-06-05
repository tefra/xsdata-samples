from dataclasses import dataclass, field
from typing import List
from voko.models.tld import Tld


@dataclass(kw_only=True)
class Ts:
    class Meta:
        name = "ts"

    content: List[object] = field(
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
        }
    )
