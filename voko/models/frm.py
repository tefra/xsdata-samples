from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.g import G
from voko.models.k import K
from voko.models.sub import Sub
from voko.models.sup import Sup


@dataclass(kw_only=True)
class Frm:
    class Meta:
        name = "frm"

    am: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
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
                    "type": G,
                },
                {
                    "name": "k",
                    "type": K,
                },
            ),
        },
    )
