from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class FacetOrderTypeEnum(Enum):
    VALUE_ASC = "VALUE_ASC"
    VALUE_DESC = "VALUE_DESC"
    COUNT_ASC = "COUNT_ASC"
    COUNT_DESC = "COUNT_DESC"
    TERM = "TERM"
    REVERSE_TERM = "REVERSE_TERM"
    COUNT = "COUNT"
    REVERSE_COUNT = "REVERSE_COUNT"
