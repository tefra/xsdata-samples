from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class LanguageType:
    class Meta:
        name = "languageType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\w){2,4}",
        }
    )
