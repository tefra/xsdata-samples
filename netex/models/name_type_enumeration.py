from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NameTypeEnumeration(Enum):
    ALIAS = "alias"
    TRANSLATION = "translation"
    COPY = "copy"
    LABEL = "label"
    OTHER = "other"
