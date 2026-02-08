from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NaturalLanguageStringStructure:
    value: str = field(
        default="",
        metadata={
            "min_length": 1,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
