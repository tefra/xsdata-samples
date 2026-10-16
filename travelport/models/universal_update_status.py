from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class UniversalUpdateStatus(StrEnum):
    ARCHIVED = "Archived"
    RETAINED = "Retained"
