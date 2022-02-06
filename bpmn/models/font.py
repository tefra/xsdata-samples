from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DC"


@dataclass
class Font:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DC"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    size: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    is_bold: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isBold",
            "type": "Attribute",
        }
    )
    is_italic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isItalic",
            "type": "Attribute",
        }
    )
    is_underline: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isUnderline",
            "type": "Attribute",
        }
    )
    is_strike_through: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isStrikeThrough",
            "type": "Attribute",
        }
    )
