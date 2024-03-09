from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class StreamingStatusValue(Enum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    UNSET = "UNSET"
