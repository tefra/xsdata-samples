from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NaturalLanguagePlaceNameStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[^,\[\]\{\}\?$%\^=@#;:]+",
        },
    )
    lang: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
