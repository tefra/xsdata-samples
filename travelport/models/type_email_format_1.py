from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeEmailFormat1(Enum):
    """Specifies the email format.

    (ie. HTML, Text, PDF, etc.)
    """

    HTML = "HTML"
    PDF = "PDF"
    PLAIN_TEXT = "Plain Text"
