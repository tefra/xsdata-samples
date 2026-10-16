from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class StreamingStatusValue(StrEnum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    UNSET = "UNSET"
