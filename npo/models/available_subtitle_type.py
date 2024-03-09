from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AvailableSubtitleType:
    class Meta:
        name = "availableSubtitleType"

    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
