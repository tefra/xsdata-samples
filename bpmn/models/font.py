from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DC"


@dataclass(kw_only=True)
class Font:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DC"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    size: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_bold: None | bool = field(
        default=None,
        metadata={
            "name": "isBold",
            "type": "Attribute",
        },
    )
    is_italic: None | bool = field(
        default=None,
        metadata={
            "name": "isItalic",
            "type": "Attribute",
        },
    )
    is_underline: None | bool = field(
        default=None,
        metadata={
            "name": "isUnderline",
            "type": "Attribute",
        },
    )
    is_strike_through: None | bool = field(
        default=None,
        metadata={
            "name": "isStrikeThrough",
            "type": "Attribute",
        },
    )
