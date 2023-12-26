from dataclasses import dataclass, field
from typing import List


@dataclass(kw_only=True)
class Sub:
    class Meta:
        name = "sub"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "g",
                    "type": str,
                },
                {
                    "name": "k",
                    "type": str,
                },
            ),
        },
    )
