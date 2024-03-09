from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GenreType1:
    class Meta:
        name = "genreType"

    term: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"3(\.[0-9]+)+",
        },
    )
