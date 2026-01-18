from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DC"


@dataclass
class Font:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DC"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    size: float | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_bold: bool | None = field(
        default=None,
        metadata={
            "name": "isBold",
            "type": "Attribute",
        },
    )
    is_italic: bool | None = field(
        default=None,
        metadata={
            "name": "isItalic",
            "type": "Attribute",
        },
    )
    is_underline: bool | None = field(
        default=None,
        metadata={
            "name": "isUnderline",
            "type": "Attribute",
        },
    )
    is_strike_through: bool | None = field(
        default=None,
        metadata={
            "name": "isStrikeThrough",
            "type": "Attribute",
        },
    )
