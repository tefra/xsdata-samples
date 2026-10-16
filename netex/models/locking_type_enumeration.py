from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingTypeEnumeration(StrEnum):
    KEY = "key"
    KEYBOARD = "keyboard"
    MECHANICAL_NUMBERING = "mechanicalNumbering"
    CONTACTLESS = "contactless"
    MOBILE_APP = "mobileApp"
    OTHER = "other"
