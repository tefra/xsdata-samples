from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class UniversalUpdateStatus(Enum):
    ARCHIVED = "Archived"
    RETAINED = "Retained"