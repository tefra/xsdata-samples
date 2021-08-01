from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GenreType1:
    class Meta:
        name = "genreType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"3(\.[0-9]+)+",
        }
    )
