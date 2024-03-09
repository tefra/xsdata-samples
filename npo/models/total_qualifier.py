from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class TotalQualifier(Enum):
    EQUAL_TO = "EQUAL_TO"
    APPROXIMATE = "APPROXIMATE"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    MISSING = "MISSING"
