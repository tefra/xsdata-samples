from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class GenreType2:
    class Meta:
        name = "genreType"

    term: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    display_name: None | str = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
