from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class PlatformTypeEnum(StrEnum):
    INTERNETVOD = "INTERNETVOD"
    TVVOD = "TVVOD"
    PLUSVOD = "PLUSVOD"
    NPOPLUSVOD = "NPOPLUSVOD"
