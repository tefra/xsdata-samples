from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class LocationTypeEnum(StrEnum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    UNKNOWN = "UNKNOWN"
