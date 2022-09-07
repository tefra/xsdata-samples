from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class BookBookType(Enum):
    EDITED_BOOK = "edited_book"
    MONOGRAPH = "monograph"
    REFERENCE = "reference"
    OTHER = "other"
