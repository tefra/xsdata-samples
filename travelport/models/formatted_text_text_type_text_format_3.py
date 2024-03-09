from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class FormattedTextTextTypeTextFormat3(Enum):
    """
    Properties
    ----------
    PLAIN_TEXT
        Textual data that is in ASCII format.
    HTML
        HTML formatted text.
    """

    PLAIN_TEXT = "PlainText"
    HTML = "HTML"
