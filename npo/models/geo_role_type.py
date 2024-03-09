from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class GeoRoleType(Enum):
    RECORDED_IN = "RECORDED_IN"
    SUBJECT = "SUBJECT"
    PRODUCED_IN = "PRODUCED_IN"
    UNDEFINED = "UNDEFINED"
