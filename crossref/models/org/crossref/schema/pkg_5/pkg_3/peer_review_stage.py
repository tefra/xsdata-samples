from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class PeerReviewStage(Enum):
    PRE_PUBLICATION = "pre-publication"
    POST_PUBLICATION = "post-publication"
