from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:api:2013"


class StandardMatchType(StrEnum):
    TEXT = "TEXT"
    REGEX = "REGEX"
    WILDCARD = "WILDCARD"
