from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class GtaaStatusType(Enum):
    CANDIDATE = "candidate"
    APPROVED = "approved"
    REDIRECTED = "redirected"
    NOT_COMPLIANT = "not_compliant"
    REJECTED = "rejected"
    OBSOLETE = "obsolete"
    DELETED = "deleted"
