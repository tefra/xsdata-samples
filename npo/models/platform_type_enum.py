from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class PlatformTypeEnum(Enum):
    INTERNETVOD = "INTERNETVOD"
    TVVOD = "TVVOD"
    PLUSVOD = "PLUSVOD"
    NPOPLUSVOD = "NPOPLUSVOD"
