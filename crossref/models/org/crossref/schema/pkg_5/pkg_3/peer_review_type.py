from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class PeerReviewType(StrEnum):
    REFEREE_REPORT = "referee-report"
    EDITOR_REPORT = "editor-report"
    AUTHOR_COMMENT = "author-comment"
    COMMUNITY_COMMENT = "community-comment"
    MANUSCRIPT = "manuscript"
    AGGREGATE = "aggregate"
    RECOMMENDATION = "recommendation"
