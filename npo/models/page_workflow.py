from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:pages:2013"


class PageWorkflow(StrEnum):
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"
