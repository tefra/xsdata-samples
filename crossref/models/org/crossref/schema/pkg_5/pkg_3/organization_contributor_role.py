from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class OrganizationContributorRole(Enum):
    AUTHOR = "author"
    EDITOR = "editor"
    CHAIR = "chair"
    REVIEWER = "reviewer"
    REVIEW_ASSISTANT = "review-assistant"
    STATS_REVIEWER = "stats-reviewer"
    REVIEWER_EXTERNAL = "reviewer-external"
    READER = "reader"
    TRANSLATOR = "translator"
