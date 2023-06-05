from dataclasses import dataclass, field
from typing import List, Optional
from voko.models.art import Art


@dataclass(kw_only=True)
class Sekcio:
    class Meta:
        name = "sekcio"

    lit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    art: List[Art] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
