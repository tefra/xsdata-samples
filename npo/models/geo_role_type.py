from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class GeoRoleType(StrEnum):
    RECORDED_IN = "RECORDED_IN"
    SUBJECT = "SUBJECT"
    PRODUCED_IN = "PRODUCED_IN"
    UNDEFINED = "UNDEFINED"
