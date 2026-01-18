from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingTypeEnumeration(Enum):
    KEY = "key"
    KEYBOARD = "keyboard"
    MECHANICAL_NUMBERING = "mechanicalNumbering"
    CONTACTLESS = "contactless"
    MOBILE_APP = "mobileApp"
    OTHER = "other"
