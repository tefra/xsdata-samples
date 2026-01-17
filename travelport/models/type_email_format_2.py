from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeEmailFormat2(Enum):
    """
    Specifies the email format. (ie.

    HTML, Text, PDF, etc.).
    """

    HTML = "HTML"
    PDF = "PDF"
    PLAIN_TEXT = "Plain Text"
