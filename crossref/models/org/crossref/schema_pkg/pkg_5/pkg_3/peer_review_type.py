from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class PeerReviewType(Enum):
    REFEREE_REPORT = "referee-report"
    EDITOR_REPORT = "editor-report"
    AUTHOR_COMMENT = "author-comment"
    COMMUNITY_COMMENT = "community-comment"
    MANUSCRIPT = "manuscript"
    AGGREGATE = "aggregate"
    RECOMMENDATION = "recommendation"
