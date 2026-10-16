from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PublicityChannelEnumeration(StrEnum):
    ALL = "all"
    PRINTED_MEDIA = "printedMedia"
    DYNAMIC_MEDIA = "dynamicMedia"
    NONE = "none"
