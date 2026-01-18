from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class PostedContentType(Enum):
    PREPRINT = "preprint"
    WORKING_PAPER = "working_paper"
    LETTER = "letter"
    DISSERTATION = "dissertation"
    REPORT = "report"
    REVIEW = "review"
    OTHER = "other"
