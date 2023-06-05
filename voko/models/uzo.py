from dataclasses import dataclass, field
from typing import List, Optional
from voko.models.tld import Tld
from voko.models.uzo_tip import UzoTip


@dataclass(kw_only=True)
class Uzo:
    class Meta:
        name = "uzo"

    tip: Optional[UzoTip] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
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
