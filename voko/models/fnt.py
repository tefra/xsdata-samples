from dataclasses import dataclass, field
from typing import List
from voko.models.lok import Lok
from voko.models.url import Url
from voko.models.vrk import Vrk


@dataclass(kw_only=True)
class Fnt:
    class Meta:
        name = "fnt"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bib",
                    "type": str,
                },
                {
                    "name": "aut",
                    "type": str,
                },
                {
                    "name": "vrk",
                    "type": Vrk,
                },
                {
                    "name": "lok",
                    "type": Lok,
                },
                {
                    "name": "url",
                    "type": Url,
                },
            ),
        }
    )
