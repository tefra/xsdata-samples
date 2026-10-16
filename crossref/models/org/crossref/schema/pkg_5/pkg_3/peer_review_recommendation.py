from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class PeerReviewRecommendation(StrEnum):
    MAJOR_REVISION = "major-revision"
    MINOR_REVISION = "minor-revision"
    REJECT = "reject"
    REJECT_WITH_RESUBMIT = "reject-with-resubmit"
    ACCEPT = "accept"
    ACCEPT_WITH_RESERVATION = "accept-with-reservation"
