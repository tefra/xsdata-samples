from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class LanguageType:
    class Meta:
        name = "languageType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\w){2,4}",
        },
    )
