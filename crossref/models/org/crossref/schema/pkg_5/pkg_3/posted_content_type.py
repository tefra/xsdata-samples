from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class PostedContentType(StrEnum):
    PREPRINT = "preprint"
    WORKING_PAPER = "working_paper"
    LETTER = "letter"
    DISSERTATION = "dissertation"
    REPORT = "report"
    REVIEW = "review"
    OTHER = "other"
