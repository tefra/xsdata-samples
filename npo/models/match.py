from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class Match(Enum):
    MUST = "MUST"
    SHOULD = "SHOULD"
    NOT = "NOT"
