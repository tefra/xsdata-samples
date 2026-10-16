from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ContentItemComponentType(StrEnum):
    CHAPTER = "chapter"
    SECTION = "section"
    PART = "part"
    TRACK = "track"
    REFERENCE_ENTRY = "reference_entry"
    OTHER = "other"
