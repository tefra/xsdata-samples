from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LimitationStatusEnumeration(StrEnum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    PARTIAL = "partial"
