from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ContentItemPublicationType(Enum):
    ABSTRACT_ONLY = "abstract_only"
    FULL_TEXT = "full_text"
    BIBLIOGRAPHIC_RECORD = "bibliographic_record"
