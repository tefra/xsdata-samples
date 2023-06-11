from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class LocationTypeEnum(Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    UNKNOWN = "UNKNOWN"
