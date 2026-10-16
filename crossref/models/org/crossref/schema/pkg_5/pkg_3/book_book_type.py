from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class BookBookType(StrEnum):
    EDITED_BOOK = "edited_book"
    MONOGRAPH = "monograph"
    REFERENCE = "reference"
    OTHER = "other"
