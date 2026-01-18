from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.formatted_text_text_type_text_format_5 import (
    FormattedTextTextTypeTextFormat5,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class FormattedTextTextType5:
    """
    Provides text and indicates whether it is formatted or not.

    Parameters
    ----------
    value
    formatted
        Textual information, which may be formatted as a line of
        information, or unformatted, as a paragraph of text.
    language
        Language identification.
    text_format
        Indicates the format of text used in the description e.g.
        unformatted  or html.
    """

    class Meta:
        name = "FormattedTextTextType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    formatted: None | bool = field(
        default=None,
        metadata={
            "name": "Formatted",
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
        },
    )
    text_format: None | FormattedTextTextTypeTextFormat5 = field(
        default=None,
        metadata={
            "name": "TextFormat",
            "type": "Attribute",
        },
    )
