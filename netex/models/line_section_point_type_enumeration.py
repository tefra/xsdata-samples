from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LineSectionPointTypeEnumeration(StrEnum):
    NORMAL = "normal"
    INTERCHANGE = "interchange"
    MAJOR_INTERCHANGE = "majorInterchange"
    TERMINUS = "terminus"
    MAJOR_TERMINUS = "majorTerminus"
    OTHER = "other"
