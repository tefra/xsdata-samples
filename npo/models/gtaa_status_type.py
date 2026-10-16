from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class GtaaStatusType(StrEnum):
    CANDIDATE = "candidate"
    APPROVED = "approved"
    REDIRECTED = "redirected"
    NOT_COMPLIANT = "not_compliant"
    REJECTED = "rejected"
    OBSOLETE = "obsolete"
    DELETED = "deleted"
