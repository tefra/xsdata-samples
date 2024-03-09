from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:shared:2009"


class OwnerTypeEnum(Enum):
    BROADCASTER = "BROADCASTER"
    NEBO = "NEBO"
    NPO = "NPO"
    MIS = "MIS"
    CERES = "CERES"
    PLUTO = "PLUTO"
    PROJECTM = "PROJECTM"
    WHATS_ON = "WHATS_ON"
    IMMIX = "IMMIX"
    AUTHORITY = "AUTHORITY"
    RADIOBOX = "RADIOBOX"
    BEELDENGELUID = "BEELDENGELUID"
