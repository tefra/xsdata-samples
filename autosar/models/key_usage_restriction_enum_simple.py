from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class KeyUsageRestrictionEnumSimple(Enum):
    GENERATE = "GENERATE"
    GENERATE_AND_VERIFY = "GENERATE-AND-VERIFY"
    VERIFY = "VERIFY"
