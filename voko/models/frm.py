from dataclasses import dataclass, field
from typing import List, Optional
from voko.models.sub import Sub
from voko.models.sup import Sup


@dataclass(kw_only=True)
class Frm:
    class Meta:
        name = "frm"

    am: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
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
