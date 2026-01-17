from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FreeTextType:
    """
    Textual information to provide descriptions and/or additional
    information.

    Attributes:
        value:
        language: Language identification.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
        },
    )
