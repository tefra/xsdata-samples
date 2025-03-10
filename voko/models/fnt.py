from dataclasses import dataclass, field

from voko.models.aut import Aut
from voko.models.bib import Bib
from voko.models.lok import Lok
from voko.models.url import Url
from voko.models.vrk import Vrk


@dataclass(kw_only=True)
class Fnt:
    class Meta:
        name = "fnt"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bib",
                    "type": Bib,
                },
                {
                    "name": "aut",
                    "type": Aut,
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
        },
    )
