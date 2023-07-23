from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class ContentProviderAgencyCredentials(Enum):
    REQUIRED = "Required"
    OPTIONAL = "Optional"
    PROHIBITED = "Prohibited"
